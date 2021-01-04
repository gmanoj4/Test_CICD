# -*- coding: utf-8 -*-
from user_voice_search import speak
from voice_to_test import voice_to_test
from google_search_for_test import google_serach
from extract_hs_code import extract_HS_Code

if __name__== "__main__":
    """Main Function to call all functions
    and display final HS-Code for user.
    """
    res1 = speak()
    print(res1)
    res2 = voice_to_test(res1)
    print(res2)
    res3 = google_serach(res2)
    print(res3)
    res4 = extract_HS_Code(res3)
    print(res4)
print(__name__== "__main__".__doc__ )