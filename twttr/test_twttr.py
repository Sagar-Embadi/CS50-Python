# test the upper and lower casses
def test_upper_lower_cases():
    assert shorten('twitter') == 'twttr'
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('TwItTeR') == 'TwtTR'

# test number cases
def test_number_cases():
    assert shorten('12345') == '12345'

# test punctuation cases
def test_punctuation_cases():
    assert shorten('!@#$') == '!@#$'

if __name__ == "__main__":
    main()
