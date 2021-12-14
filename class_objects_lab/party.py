class Party:
    def __init__(self):
        self.people = []

    def __get_info__(self):
        all_participants = self.people
        participants_result = (", ".join(self.people))
        return f"""Going: {participants_result}
Total: {len(all_participants)}"""

man_input = input()
party = Party()
while man_input != "End":
    party.people.append(man_input)
    man_input = input()

info = party.__get_info__()
print(info)
