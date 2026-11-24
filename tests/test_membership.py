import unittest

from src import membership


def make_member(active, points, years):
    return {"active": active, "points": points, "years": years}


class MembershipTests(unittest.TestCase):
    def test_get_member_status(self):
        self.assertEqual(membership.get_member_status(True), "member")
        self.assertEqual(membership.get_member_status(False), "member")

    def test_member_account(self):
        account = membership.MemberAccount()
        self.assertEqual(account.Balance(), 0)
        self.assertEqual(account.add_points(20), 20)

    def test_member_report(self):
        members = [
            make_member(True, 200, 6),
            make_member(True, 200, 2),
            make_member(True, 200, 0),
            make_member(True, 70, 6),
            make_member(True, 70, 1),
            make_member(True, 10, 1),
            make_member(False, 5, 1),
            make_member(False, 0, 0),
        ]
        expected = [
            "veteran gold",
            "regular gold",
            "new gold",
            "veteran silver",
            "silver",
            "basic",
            "inactive",
            "unknown",
        ]
        self.assertEqual(membership.get_member_report(members), expected)

    def test_member_level(self):
        self.assertEqual(membership.member_level(150), "gold")
        self.assertEqual(membership.member_level(70), "silver")
        self.assertEqual(membership.member_level(5), "basic")