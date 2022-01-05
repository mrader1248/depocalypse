from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .utils import create_commodity_with_transactions
from ..views.calorific_value_outlook import calorific_value_outlook


class CalorificValueOutlookTests(TestCase):
    """
    This `TestCase` class is testing the API function
    `calorific_value_outlook`.
    """

    def _call_calorific_value_outlook(self):
        response = self.client.get(reverse(calorific_value_outlook))
        self.assertEqual(response.status_code, 200)
        self._response = response.json()
        self.assertIn('dates', self._response)
        self.assertIn('calorificValues', self._response)

    def _assert_dates(self, expected_dates):
        self.assertEqual(
            self._response['dates'],
            [date.isoformat()[:10] for date in expected_dates]
        )

    def _assert_calorific_values(self, expected_calorific_values):
        self.assertEqual(
            self._response['calorificValues'],
            expected_calorific_values
        )

    def test_empty_database(self):
        """
        If `calorific_value_outlook` is called for an empty DB, it must return
        today as the only day with zero calorific value.
        """
        self._call_calorific_value_outlook()
        self._assert_dates([timezone.now().date()])
        self._assert_calorific_values([0])

    def test_commodity_without_transactions(self):
        """
        If there is a single commodity without any transactions,
        `calorific_value_outlook` must return empty lists.
        """
        create_commodity_with_transactions('Testaghetti', 1234, [])
        self._call_calorific_value_outlook()
        self._assert_dates([timezone.now().date()])
        self._assert_calorific_values([0])

    def test_multiple_commodities_and_best_before_dates(self):
        """
                                |   -1  | today |   +1  |   +2  |   +3
        ------------------------+-------+-------+-------+-------+-------
        Testaghetti (1000 kcal) |   +1  |       |   -1  |       |
          best before day +1    |       |       |       |       |
        ------------------------+-------+-------+-------+-------+-------
        Testaghetti (1000 kcal) |   +2  |       |       |   -2  |
          best before day +2    |       |       |       |       |
        ------------------------+-------+-------+-------+-------+-------
        Testaghetti (1000 kcal) |   +2  |       |       |       |   -2
          best before day +3    |       |       |       |       |
        ------------------------+-------+-------+-------+-------+-------
        Testiatelle (100 kcal)  |   +4  |       |   -4  |       |
          best before day +1    |       |       |       |       |
        ------------------------+-------+-------+-------+-------+-------
        Testiatelle (100 kcal)  |   +4  |       |       |   -4  |
          best before day +2    |       |       |       |       |
        ------------------------+-------+-------+-------+-------+-------
        change (kcal)           | +5800 |       | -1100 | -2400 | -2000
        total (kcal)            |  5800 |       |  4400 |  2000 |     0
        """
        now = timezone.now()
        today = now.date()
        transaction_timestamp = now - timezone.timedelta(days=1)
        best_before_dates = [
            today + timezone.timedelta(weeks=n_weeks)
            for n_weeks in [1, 2, 3]
        ]
        create_commodity_with_transactions("Testaghetti", 1000, [
            (transaction_timestamp, 1, best_before_dates[0]),
            (transaction_timestamp, 2, best_before_dates[1]),
            (transaction_timestamp, 3, best_before_dates[2]),
            (transaction_timestamp, -1, best_before_dates[2])
        ])
        create_commodity_with_transactions("Testiatelle", 100, [
            (transaction_timestamp, 4, best_before_dates[1]),
            (transaction_timestamp, 4, best_before_dates[0])
        ])
        self._call_calorific_value_outlook()
        self._assert_dates([today] + best_before_dates)
        self._assert_calorific_values([5800, 4400, 2000, 0])

    def test_future_transaction_timestamps(self):
        """
                                | today |  +1  |  +2  |  +3  |  +4  |  +5
        ------------------------+-------+------+------+------+------+------
        Testaghetti (1000 kcal) |       |  +1  |  +2  |  +3  |      |  -6
          best before day +7    |       |      |      |      |      |
        ------------------------+-------+------+------+------+------+------
        change (kcal)           |       | +100 | +200 | +300 |      | -600
        total (kcal)            |       |  100 |  300 |  600 |      |    0
        """
        now = timezone.now()
        today = now.date()
        transaction_timestamps = [
            now + timezone.timedelta(days=n_days)
            for n_days in [1, 2, 3]
        ]
        best_before_date = today + timezone.timedelta(days=5)
        create_commodity_with_transactions("Testaghetti", 100, [
            (transaction_timestamps[0], 1, best_before_date),
            (transaction_timestamps[1], 2, best_before_date),
            (transaction_timestamps[2], 3, best_before_date)
        ])
        self._call_calorific_value_outlook()
        self._assert_dates([today] + transaction_timestamps + [best_before_date])
        self._assert_calorific_values([0, 100, 300, 600, 0])

    def test_past_and_future_transaction_timestamps(self):
        """
                                |  -2  |  -1  | today |  +1  |  +2  |  +3
        ------------------------+------+------+-------+------+------+------
        Testaghetti (1000 kcal) |  +1  |  +2  |   +3  |  +4  |  +5  |  -15
          best before day +7    |      |      |       |      |      |
        ------------------------+------+------+-------+------+------+------
        change (kcal)           | +100 | +200 |  +300 | +400 | +500 | -1500
        total (kcal)            |  100 |  300 |   600 | 1000 | 1500 |     0
        """
        now = timezone.now()
        today = now.date()
        transaction_timestamps = [
            now + timezone.timedelta(days=n_days)
            for n_days in range(-2, 3)
        ]
        best_before_date = today + timezone.timedelta(days=3)
        create_commodity_with_transactions("Testaghetti", 100, [
            (transaction_timestamp, j + 1, best_before_date)
            for j, transaction_timestamp in enumerate(transaction_timestamps)
        ])
        self._call_calorific_value_outlook()
        self._assert_dates(transaction_timestamps[2:] + [best_before_date])
        self._assert_calorific_values([600, 1000, 1500, 0])
