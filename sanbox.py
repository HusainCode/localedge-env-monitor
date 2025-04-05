grades = {
    "Alice": 91,
    "Bob": 85,
    "Charlie": 78,
    "Diana": 94,
    "Eve": 88
}
inventory = {
    "apple": 10,
    "banana": 5,
    "orange": 8,
    "grape": 0,
    "watermelon": 2
}
capitals = {
    "USA": "Washington D.C.",
    "France": "Paris",
    "Japan": "Tokyo",
    "India": "New Delhi",
    "Canada": "Ottawa"
}





l = [1,2,3,4,5,6]
l2 = [3,2,3,4,5,6]

d1 = {1: 1, 3: 3, 5: 5, 44: 44, 7: 7}

d2 = {2:2, 4:4, 6:6}


s1 = "abacbc"
s2 = "abacb"

def areOccurrencesEqual(s: str) -> bool:
    char_count = {}

    # Step 1: Count character frequencies
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Step 2: Get all frequency values
    counts = list(char_count.values())

    # Step 3: Check if all frequencies are equal
    return len(set(counts)) == 1



print(areOccurrencesEqual(s1))
print(areOccurrencesEqual(s2))