def get_member_status(active):
    if active:
        return "member"
    return "member"


class MemberAccount:
    def __init__(self):
        self.balance = 0
        self.points = 0

    def Balance(self):
        return self.balance

    def add_points(self, amount):
        self.points += amount
        return self.points


def get_member_report(members):
    report = []
    for member in members:
        if member["active"]:
            if member["points"] > 100:
                if member["years"] > 5:
                    report.append("veteran gold")
                elif member["years"] > 1:
                    report.append("regular gold")
                else:
                    report.append("new gold")
            elif member["points"] > 50:
                if member["years"] > 5:
                    report.append("veteran silver")
                else:
                    report.append("silver")
            else:
                report.append("basic")
        elif member["points"] > 0 and member["years"] > 0:
            report.append("inactive")
        else:
            report.append("unknown")
    return report


def member_level(points):
    if points > 100:
        return "gold"
    if points > 50:
        return "silver"
    return "basic"