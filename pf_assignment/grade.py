from Ex1 import makeHappiness
from Ex2 import calculateHappinessScore
from Ex3 import findHappinestNumber
from Ex4 import maximizeHappiestScore
from Ex5 import Member, splitGroups
import signal
from contextlib import contextmanager


class TimeoutException(Exception):
    pass


@contextmanager
def time_limit(seconds):
    def signal_handler(signum, frame):
        raise RuntimeWarning("Timed out!")
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)
    try:
        yield
    except Warning as e:
        print(e)
    finally:
        signal.alarm(0)


# EX1
score = 0
if makeHappiness("") == "Happy ":
    score += 1
if makeHappiness("Andy") == "Happy Andy":
    score += 1
if makeHappiness("1234") == "Happy 1234":
    score += 1
if makeHappiness(" ABCD 1234") == "Happy  ABCD 1234":
    score += 1
if makeHappiness(" 1234\nABCD 1234\n ") == "Happy  1234\nABCD 1234\n ":
    score += 1

print("Ex1 Score: ", score, "/", 5)

# EX2
score = 0
if calculateHappinessScore("Hello, World!") == "Happiness Score: 323 (Happy)":
    score += 1
if calculateHappinessScore("Sad") == "Happiness Score: 97 (Unhappy)":
    score += 1
if calculateHappinessScore("") == "Happiness Score: 0 (Unhappy)":
    score += 1
if calculateHappinessScore("aoeiu") == "Happiness Score: 531 (Happy)":
    score += 1
if calculateHappinessScore("a o e i u") == "Happiness Score: 531 (Happy)":
    score += 1
if calculateHappinessScore("aA oO uU iI eE") == "Happiness Score: 902 (Happy)":
    score += 1
if calculateHappinessScore("bcaAabc deoOed udeU iyhI eikE") == "Happiness Score: 1407 (Happy)":
    score += 1
if calculateHappinessScore("l aaaaaa l") == "Happiness Score: 582 (Happy)":
    score += 1
if calculateHappinessScore("El aaaaaa lO") == "Happiness Score: 730 (Happy)":
    score += 1
if calculateHappinessScore("BCDF bcdf") == "Happiness Score: 0 (Unhappy)":
    score += 1

print("Ex2 Score: ", score, "/", 10)

# EX3
score = 0
if findHappinestNumber("13,89,53,45,67") == 53:
    score += 1
if findHappinestNumber("13,89,45,67") == 13:
    score += 1
if findHappinestNumber("13") == 13:
    score += 1
if findHappinestNumber("7207,53,13") == 7207:
    score += 1
if findHappinestNumber("13,1021,7777,13") == 1021:
    score += 1
if findHappinestNumber("") == 0:
    score += 1
if findHappinestNumber("0,1,243,6434,96232,0") == 0:
    score += 1
if findHappinestNumber("0,1202,1201,6367,0") == 1201:
    score += 1
if findHappinestNumber("5419,0,1202,6367,0,5669") == 0:
    score += 1
if findHappinestNumber("5419,0,1202,6367,0,5669,7621,5419,0,1202,6367,0,5669,5419,0,1202,6367,0,5669,7621,5419,0,1202,6367,0,5669") == 7621:
    score += 1

print("Ex3 Score: ", score, "/", 10)

# EX4
score = 0
with time_limit(5):
    if maximizeHappiestScore("i love you") == "Happiest String: e - Happiest Score: 101 (Happy)":
        score += 1
with time_limit(5):
    if maximizeHappiestScore("") == "Happiest String:  - Happiest Score: 0 (Unhappy)":
        score += 1
with time_limit(5):
    if maximizeHappiestScore("LLL IiI EeE oAo ooo") == "Happiest String: IIeiooooo - Happiest Score: 907 (Happy)":
        score += 1
with time_limit(5):
    if maximizeHappiestScore("LLL a") == "Happiest String: a - Happiest Score: 97 (Unhappy)":
        score += 1
with time_limit(5):
    if maximizeHappiestScore(" x y z xyz ") == "Happiest String: - Happiest Score: 0 (Unhappy)":
        score += 1
with time_limit(5):
    if maximizeHappiestScore(" a e i o u ") == "Happiest String: a - Happiest Score: 97 (Unhappy)":
        score += 1
with time_limit(5):
    if maximizeHappiestScore(" A E I O U ") == "Happiest String: EOU - Happiest Score: 233 (Happy)":
        score += 1
with time_limit(5):
    if maximizeHappiestScore("\neLI aAIIch") == "Happiest String: AII - Happiest Score: 211 (Happy)":
        score += 1
with time_limit(5):
    if maximizeHappiestScore(" a e i o u A E I O U ") == "Happiest String: EIaeiou - Happiest Score: 673 (Happy)":
        score += 1
with time_limit(5):
    if maximizeHappiestScore("\neLIAO\neNIN\na\na\naLO\n") == "Happiest String: AOOaaee - Happiest Score: 619 (Happy)":
        score += 1
with time_limit(5):
    if maximizeHappiestScore(" \neLI aAIIch") == "Happiest String: AII - Happiest Score: 211 (Happy)":
        score += 1.25
with time_limit(5):
    if maximizeHappiestScore(" uUu IiI EeE oAo O") == "Happiest String: AEIIOeioouu - Happiest Score: 1021 (Happy)" and maximizeHappiestScore("\neLI aAOIIch") == "Happiest String: Oae - Happiest Score: 277 (Happy)":
        score += 1.25

print("Ex4 Score: ", score, "/", 12.5)

# EX5
score = 0
members = [
    Member("Alice", 5),
    Member("Bob", 7),
    Member("Charlie", 3),
    Member("David", 8),
    Member("Eve", 6),
    Member("Frank", 4),
    Member("Grace", 9),
    Member("Henry", 2)
]
with time_limit(5):
    if len(splitGroups(members, 8, 10)) >= 4:
        score += 1
with time_limit(5):
    if len(splitGroups(members, 4, 10)) >= 2:
        score += 1
with time_limit(5):
    if splitGroups(members, 0, 10) == None:
        score += 1
with time_limit(5):
    if len(splitGroups(members, 8, 12)) >= 3:
        score += 1
members = [
    Member("Alice", 5),
    Member("Bob", 7),
    Member("Charlie", 3),
    Member("David", 8),
    Member("Eve", 6),
    Member("Frank", 4),
    Member("Grace", 9),
    Member("Henry", 2),
    Member("Ivan", 5),
    Member("Kevin", 10),
    Member("Lenna", 35),
    Member("Monich", 1),
    Member("Nick", 9),
    Member("Opus", 14),
    Member("Pepple", 8),
    Member("Quardo", 2),
]
with time_limit(5):
    if len(splitGroups(members, 16, 15)) >= 7:
        score += 1
with time_limit(5):
    if splitGroups(members, 2, 15) == None:
        score += 1
with time_limit(5):
    if len(splitGroups(members, 16, 1)) == 16:
        score += 1
with time_limit(5):
    if len(splitGroups(members, 16, -1)) == 16:
        score += 1.25
members = [
    Member("Alice", 5),
    Member("Bob", 7),
    Member("Charlie", 3),
    Member("David", 8),
    Member("Eve", 6),
    Member("Frank", 4),
    Member("Grace", 9),
    Member("Henry", 2),
    Member("Ivan", 5),
    Member("Kevin", 10),
    Member("Lenna", 35),
    Member("Lenna", 35),
    Member("Monich", 1),
    Member("Nick", 9),
    Member("Opus", 14),
    Member("Pepple", 8),
    Member("Quardo", 2),
]
with time_limit(5):
    if len(splitGroups(members, 17, 1)) == 17:
        score += 1
with time_limit(5):
    if len(splitGroups(members, 17, 13)) >= 8 and len(splitGroups(members, 10, 18)) >= 3:
        score += 1.25
members = [
    Member("Alice", 5),
    Member("Bob", 7),
    Member("Charlie", 3),
    Member("David", 8),
    Member("Eve", 6),
    Member("Frank", 4),
    Member("Grace", 9),
    Member("Henry", 2),
    Member("Ivan", 5),
    Member("Kevin", 10),
    Member("Kevin", 10),
    Member("Lenna", 35),
    Member("Monich", 1),
    Member("Nick", 9),
    Member("Opus", 14),
    Member("Pepple", 8),
    Member("Quardo", 2),
]
with time_limit(5):
    if len(splitGroups(members, 17, 5)) >= 14:
        score += 1
with time_limit(5):
    members = []
    if splitGroups(members, 0, 5) == None:
        score += 1

print("Ex5 Score: ", score, "/", 12.5)
