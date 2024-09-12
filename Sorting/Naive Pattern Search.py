def pattern_search(text, pattern):
    print("\n" + text + "\n")
    print(pattern + "\n")
    for n in range(len(text)):
        print("Text Index: {0}".format(n))
        match_count = 0
        for l in range(len(pattern)):
            print("Pattern Index: {0}".format(l))
            if pattern[l] == text[n + l]:
                print("Matching index found")
                print("Match Count: {0}".format(match_count))
                match_count += 1
            else:
                break
        if match_count == len(pattern):
            print("\n{P} found at index {I}\n".format(P = pattern, I = n))



    

text = "HAYHAYNEEDLEHAYHAYHAYNEEDLEHAYHAYHAYHAYNEEDLE"
pattern = "NEEDLE"

pattern_search(text, pattern)

text2 = "SOMEMORERANDOMWORDSTOpatternSEARCHTHROUGH"
pattern2 = "pattern"

pattern_search(text2, pattern2)

text3 = "This   still      works with    spaces"
pattern3 = "works"

pattern_search(text3, pattern3)

text4 = "722615457824612704202682179992552072047396"
pattern4 = "42"

pattern_search(text4, pattern4)
