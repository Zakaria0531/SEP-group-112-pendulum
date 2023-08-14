from .custom import translations as custom_translations


"""
he locale file.

It has been generated automatically and must not be modified directly.
"""


locale = {
    "plural": lambda n: "many"
    if (
        ((0 == 0 and (0 == 0)) and (not (n == n and (n >= 0 and n <= 10))))
        and ((n % 10) == (n % 10) and ((n % 10) == 0))
    )
    else "one"
    if ((n == n and (n == 1)) and (0 == 0 and (0 == 0)))
    else "two"
    if ((n == n and (n == 2)) and (0 == 0 and (0 == 0)))
    else "other",
    "ordinal": lambda n: "other",
    "translations": {
        "days": {
            "abbreviated": {
                0: "יום ב׳",
                1: "יום ג׳",
                2: "יום ד׳",
                3: "יום ה׳",
                4: "יום ו׳",
                5: "שבת",
                6: "יום א׳",
            },
            "narrow": {
                0: "ב׳",
                1: "ג׳",
                2: "ד׳",
                3: "ה׳",
                4: "ו׳",
                5: "ש׳",
                6: "א׳",
            },
            "short": {
                0: "ב׳",
                1: "ג׳",
                2: "ד׳",
                3: "ה׳",
                4: "ו׳",
                5: "ש׳",
                6: "א׳",
            },
            "wide": {
                0: "יום שני",
                1: "יום שלישי",
                2: "יום רביעי",
                3: "יום חמישי",
                4: "יום שישי",
                5: "יום שבת",
                6: "יום ראשון",
            },
        },
        "months": {
            "abbreviated": {
                1: "ינו׳",
                2: "פבר׳",
                3: "מרץ",
                4: "אפר׳",
                5: "מאי",
                6: "יוני",
                7: "יולי",
                8: "אוג׳",
                9: "ספט׳",
                10: "אוק׳",
                11: "נוב׳",
                12: "דצמ׳",
            },
            "narrow": {
                1: "1",
                2: "2",
                3: "3",
                4: "4",
                5: "5",
                6: "6",
                7: "7",
                8: "8",
                9: "9",
                10: "10",
                11: "11",
                12: "12",
            },
            "wide": {
                1: "ינואר",
                2: "פברואר",
                3: "מרץ",
                4: "אפריל",
                5: "מאי",
                6: "יוני",
                7: "יולי",
                8: "אוגוסט",
                9: "ספטמבר",
                10: "אוקטובר",
                11: "נובמבר",
                12: "דצמבר",
            },
        },
        "units": {
            "year": {
                "one": "שנה",
                "two": "שנתיים",
                "many": "{0} שנים",
                "other": "{0} שנים",
            },
            "month": {
                "one": "חודש",
                "two": "חודשיים",
                "many": "{0} חודשים",
                "other": "{0} חודשים",
            },
            "week": {
                "one": "שבוע",
                "two": "שבועיים",
                "many": "{0} שבועות",
                "other": "{0} שבועות",
            },
            "day": {
                "one": "יום {0}",
                "two": "יומיים",
                "many": "{0} יום",
                "other": "{0} ימים",
            },
            "hour": {
                "one": "שעה",
                "two": "שעתיים",
                "many": "{0} שעות",
                "other": "{0} שעות",
            },
            "minute": {
                "one": "דקה",
                "two": "שתי דקות",
                "many": "{0} דקות",
                "other": "{0} דקות",
            },
            "second": {
                "one": "שניה",
                "two": "שתי שניות",
                "many": "\u200f{0} שניות",
                "other": "{0} שניות",
            },
            "microsecond": {
                "one": "{0} מיליונית שנייה",
                "two": "{0} מיליוניות שנייה",
                "many": "{0} מיליוניות שנייה",
                "other": "{0} מיליוניות שנייה",
            },
        },
        "relative": {
            "year": {
                "future": {
                    "other": "בעוד {0} שנים",
                    "one": "בעוד שנה",
                    "two": "בעוד שנתיים",
                    "many": "בעוד {0} שנה",
                },
                "past": {
                    "other": "לפני {0} שנים",
                    "one": "לפני שנה",
                    "two": "לפני שנתיים",
                    "many": "לפני {0} שנה",
                },
            },
            "month": {
                "future": {
                    "other": "בעוד {0} חודשים",
                    "one": "בעוד חודש",
                    "two": "בעוד חודשיים",
                    "many": "בעוד {0} חודשים",
                },
                "past": {
                    "other": "לפני {0} חודשים",
                    "one": "לפני חודש",
                    "two": "לפני חודשיים",
                    "many": "לפני {0} חודשים",
                },
            },
            "week": {
                "future": {
                    "other": "בעוד {0} שבועות",
                    "one": "בעוד שבוע",
                    "two": "בעוד שבועיים",
                    "many": "בעוד {0} שבועות",
                },
                "past": {
                    "other": "לפני {0} שבועות",
                    "one": "לפני שבוע",
                    "two": "לפני שבועיים",
                    "many": "לפני {0} שבועות",
                },
            },
            "day": {
                "future": {
                    "other": "בעוד {0} ימים",
                    "one": "בעוד יום {0}",
                    "two": "בעוד יומיים",
                    "many": "בעוד {0} ימים",
                },
                "past": {
                    "other": "לפני {0} ימים",
                    "one": "לפני יום {0}",
                    "two": "לפני יומיים",
                    "many": "לפני {0} ימים",
                },
            },
            "hour": {
                "future": {
                    "other": "בעוד {0} שעות",
                    "one": "בעוד שעה",
                    "two": "בעוד שעתיים",
                    "many": "בעוד {0} שעות",
                },
                "past": {
                    "other": "לפני {0} שעות",
                    "one": "לפני שעה",
                    "two": "לפני שעתיים",
                    "many": "לפני {0} שעות",
                },
            },
            "minute": {
                "future": {
                    "other": "בעוד {0} דקות",
                    "one": "בעוד דקה",
                    "two": "בעוד שתי דקות",
                    "many": "בעוד {0} דקות",
                },
                "past": {
                    "other": "לפני {0} דקות",
                    "one": "לפני דקה",
                    "two": "לפני שתי דקות",
                    "many": "לפני {0} דקות",
                },
            },
            "second": {
                "future": {
                    "other": "בעוד {0} שניות",
                    "one": "בעוד שנייה",
                    "two": "בעוד שתי שניות",
                    "many": "בעוד {0} שניות",
                },
                "past": {
                    "other": "לפני {0} שניות",
                    "one": "לפני שנייה",
                    "two": "לפני שתי שניות",
                    "many": "לפני {0} שניות",
                },
            },
        },
        "day_periods": {
            "midnight": "חצות",
            "am": "לפנה״צ",
            "pm": "אחה״צ",
            "morning1": "בבוקר",
            "afternoon1": "בצהריים",
            "afternoon2": "אחר הצהריים",
            "evening1": "בערב",
            "night1": "בלילה",
            "night2": "לפנות בוקר",
        },
        "week_data": {
            "min_days": 1,
            "first_day": 0,
            "weekend_start": 5,
            "weekend_end": 6,
        },
    },
    "custom": custom_translations,
}
