"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
def main():
    score = get_score()
    if score > 100:
        print("Invalid score")
    if 50 < score < 90:
        print("Passable")
    if 100 >= score > 90:
        print("Excellent")
    if score < 50:
        print("Bad")


def get_score():
    score = float(input("Enter score: "))
    return score


main()