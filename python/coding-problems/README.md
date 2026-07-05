# Coding Problems

Solutions to coding problems from platforms like LeetCode, HackerRank, CodeSignal, and AlgoExpert.

## Structure

Problems are organized into subfolders by platform:

| Folder | Platform | Numbering scheme |
|---|---|---|
| `leetcode/` | LeetCode | Canonical LeetCode problem number (e.g. `128_longest_consecutive_sequence.py` = #128) |
| `hackerrank/` | HackerRank | Sequential (001, 002, …) in order added |
| `codesignal/` | CodeSignal | Sequential (001, 002, …) in order added |
| `misc/` | AlgoExpert / other / no source | Sequential (001, 002, …) |

Each file includes a comment at the top linking to the original problem on its platform.

## Tests

Selected solutions have pytest test cases in [tests/](tests/). To run them from the `python/` directory:

```bash
uv run pytest
```

New solutions should come with a test file; use the existing ones as a template. The
`load_solution()` helper in [tests/conftest.py](tests/conftest.py) imports a solution
by file path (needed because the filenames start with digits).

## Solutions Index

This index is generated from the files on disk, so don't edit it by hand. To regenerate after adding a solution:

```bash
uv run python coding-problems/generate_index.py
```

<!-- BEGIN GENERATED INDEX (run generate_index.py) -->

**149 problems solved so far.**

### LeetCode (38 solved)

| # | Problem | Solution |
|---|---------|----------|
| 002 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/description/) | [002_add_two_numbers.py](leetcode/002_add_two_numbers.py) |
| 007 | [Reverse Integer](https://leetcode.com/problems/reverse-integer/?envType=company&envId=linkedin&favoriteSlug=linkedin-six-months) | [007_reverse_integer.py](leetcode/007_reverse_integer.py) |
| 026 | [Remove Duplicates From Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/) | [026_remove_duplicates_from_sorted_array.py](leetcode/026_remove_duplicates_from_sorted_array.py) |
| 027 | [Remove Element](https://leetcode.com/problems/remove-element/) | [027_remove_element.py](leetcode/027_remove_element.py) |
| 034 | [Find First And Last Position Of Element In Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) | [034_find_first_and_last_position_of_element_in_sorted_array.py](leetcode/034_find_first_and_last_position_of_element_in_sorted_array.py) |
| 054 | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/) | [054_spiral_matrix.py](leetcode/054_spiral_matrix.py) |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | [125_valid_palindrome.py](leetcode/125_valid_palindrome.py) |
| 128 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | [128_longest_consecutive_sequence.py](leetcode/128_longest_consecutive_sequence.py) |
| 463 | [Island Perimeter](https://leetcode.com/problems/island-perimeter/?envType=problem-list-v2&envId=matrix) | [463_island_perimeter.py](leetcode/463_island_perimeter.py) |
| 566 | [Reshape The Matrix](https://leetcode.com/problems/reshape-the-matrix/description/?envType=problem-list-v2&envId=matrix) | [566_reshape_the_matrix.py](leetcode/566_reshape_the_matrix.py) |
| 645 | [Set Mismatch](https://leetcode.com/problems/set-mismatch/?envType=daily-question&envId=2024-01-22) | [645_set_mismatch.py](leetcode/645_set_mismatch.py) |
| 661 | [Image Smoother](https://leetcode.com/problems/image-smoother/description/?envType=problem-list-v2&envId=matrix) | [661_image_smoother.py](leetcode/661_image_smoother.py) |
| 1290 | [Convert Binary Number In A Linked List To Integer](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/) | [1290_convert_binary_number_in_a_linked_list_to_integer.py](leetcode/1290_convert_binary_number_in_a_linked_list_to_integer.py) |
| 1313 | [Decompress Run Length Encoded List](https://leetcode.com/problems/decompress-run-length-encoded-list/description/) | [1313_decompress_run_length_encoded_list.py](leetcode/1313_decompress_run_length_encoded_list.py) |
| 1365 | [How Many Numbers Are Smaller Than The Current Number](https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/) | [1365_how_many_numbers_are_smaller_than_the_current_number.py](leetcode/1365_how_many_numbers_are_smaller_than_the_current_number.py) |
| 1389 | [Create Target Array In The Given Order](https://leetcode.com/problems/create-target-array-in-the-given-order/) | [1389_create_target_array_in_the_given_order.py](leetcode/1389_create_target_array_in_the_given_order.py) |
| 1431 | [Kids With The Greatest Number Of Candies](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/) | [1431_kids_with_the_greatest_number_of_candies.py](leetcode/1431_kids_with_the_greatest_number_of_candies.py) |
| 1470 | [Shuffle The Array](https://leetcode.com/problems/shuffle-the-array/) | [1470_shuffle_the_array.py](leetcode/1470_shuffle_the_array.py) |
| 1480 | [Running Sum Of 1D Array](https://leetcode.com/problems/running-sum-of-1d-array/) | [1480_running_sum_of_1d_array.py](leetcode/1480_running_sum_of_1d_array.py) |
| 1512 | [Number Of Good Pairs](https://leetcode.com/problems/number-of-good-pairs/description/) | [1512_number_of_good_pairs.py](leetcode/1512_number_of_good_pairs.py) |
| 1528 | [Shuffle String](https://leetcode.com/problems/shuffle-string/description/) | [1528_shuffle_string.py](leetcode/1528_shuffle_string.py) |
| 1637 | [Widest Vertical Area Between Two Points Containing No Points](https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/description/) | [1637_widest_vertical_area_between_two_points_containing_no_points.py](leetcode/1637_widest_vertical_area_between_two_points_containing_no_points.py) |
| 1662 | [Check If Two String Arrays Are Equivalent](https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/) | [1662_check_if_two_string_arrays_are_equivalent.py](leetcode/1662_check_if_two_string_arrays_are_equivalent.py) |
| 1672 | [Richest Customer Wealth](https://leetcode.com/problems/richest-customer-wealth/description/) | [1672_richest_customer_wealth.py](leetcode/1672_richest_customer_wealth.py) |
| 1720 | [Decode Xored Array](https://leetcode.com/problems/decode-xored-array/) | [1720_decode_xored_array.py](leetcode/1720_decode_xored_array.py) |
| 1773 | [Count Items Matching A Rule](https://leetcode.com/problems/count-items-matching-a-rule/description/) | [1773_count_items_matching_a_rule.py](leetcode/1773_count_items_matching_a_rule.py) |
| 1816 | [Truncate Sentence](https://leetcode.com/problems/truncate-sentence/description/) | [1816_truncate_sentence.py](leetcode/1816_truncate_sentence.py) |
| 1920 | [Build Array From Permutation](https://leetcode.com/problems/build-array-from-permutation/description/) | [1920_build_array_from_permutation.py](leetcode/1920_build_array_from_permutation.py) |
| 1929 | [Concatenation Of Array](https://leetcode.com/problems/concatenation-of-array/description/) | [1929_concatenation_of_array.py](leetcode/1929_concatenation_of_array.py) |
| 2011 | [Final Value Of Variable After Performing Operations](https://leetcode.com/problems/final-value-of-variable-after-performing-operations/description/) | [2011_final_value_of_variable_after_performing_operations.py](leetcode/2011_final_value_of_variable_after_performing_operations.py) |
| 2114 | [Maximum Number Of Words Found In Sentences](https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/) | [2114_maximum_number_of_words_found_in_sentences.py](leetcode/2114_maximum_number_of_words_found_in_sentences.py) |
| 2574 | [Left And Right Sum Differences](https://leetcode.com/problems/left-and-right-sum-differences/) | [2574_left_and_right_sum_differences.py](leetcode/2574_left_and_right_sum_differences.py) |
| 2798 | [Number Of Employees Who Met The Target](https://leetcode.com/problems/number-of-employees-who-met-the-target/) | [2798_number_of_employees_who_met_the_target.py](leetcode/2798_number_of_employees_who_met_the_target.py) |
| 2824 | [Count Pairs Whose Sum Is Less Than Target](https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/) | [2824_count_pairs_whose_sum_is_less_than_target.py](leetcode/2824_count_pairs_whose_sum_is_less_than_target.py) |
| 2859 | [Sum Of Values At Indices With K Set Bits](https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/description/) | [2859_sum_of_values_at_indices_with_k_set_bits.py](leetcode/2859_sum_of_values_at_indices_with_k_set_bits.py) |
| 2942 | [Find Words Containing Character](https://leetcode.com/problems/find-words-containing-character/description/) | [2942_find_words_containing_character.py](leetcode/2942_find_words_containing_character.py) |
| 2974 | [Minimum Number Game](https://leetcode.com/problems/minimum-number-game/description/) | [2974_minimum_number_game.py](leetcode/2974_minimum_number_game.py) |
| 3159 | [Find Occurrences Of An Element In An Array](https://leetcode.com/problems/find-occurrences-of-an-element-in-an-array/) | [3159_find_occurrences_of_an_element_in_an_array.py](leetcode/3159_find_occurrences_of_an_element_in_an_array.py) |

### HackerRank (94 solved)

| # | Problem | Solution |
|---|---------|----------|
| 001 | [Alphabet Rangoli](https://www.hackerrank.com/challenges/alphabet-rangoli/problem) | [001_alphabet_rangoli.py](hackerrank/001_alphabet_rangoli.py) |
| 002 | Alternating Characters | [002_alternating_characters.py](hackerrank/002_alternating_characters.py) |
| 003 | Anagram | [003_anagram.py](hackerrank/003_anagram.py) |
| 004 | [Any Or All](https://www.hackerrank.com/challenges/any-or-all/problem) | [004_any_or_all.py](hackerrank/004_any_or_all.py) |
| 005 | [Athlete Sort](https://www.hackerrank.com/challenges/python-sort-sort/problem) | [005_athlete_sort.py](hackerrank/005_athlete_sort.py) |
| 006 | Beautiful Binary String | [006_beautiful_binary_string.py](hackerrank/006_beautiful_binary_string.py) |
| 007 | [Calendar Module](https://www.hackerrank.com/challenges/calendar-module/problem) | [007_calendar_module.py](hackerrank/007_calendar_module.py) |
| 008 | [Capitalize](https://www.hackerrank.com/challenges/capitalize/problem) | [008_capitalize.py](hackerrank/008_capitalize.py) |
| 009 | [Check Strict Superset](https://www.hackerrank.com/challenges/py-check-strict-superset) | [009_check_strict_superset.py](hackerrank/009_check_strict_superset.py) |
| 010 | [Check Subset](https://www.hackerrank.com/challenges/py-check-subset/problem) | [010_check_subset.py](hackerrank/010_check_subset.py) |
| 011 | [Class 1 Dealing With Complex Numbers](https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem) | [011_class_1_dealing_with_complex_numbers.py](hackerrank/011_class_1_dealing_with_complex_numbers.py) |
| 012 | [Collections Namedtuple](https://www.hackerrank.com/challenges/py-collections-namedtuple/problem) | [012_collections_namedtuple.py](hackerrank/012_collections_namedtuple.py) |
| 013 | [Collections Counter](https://www.hackerrank.com/challenges/collections-counter/problem) | [013_collections_counter.py](hackerrank/013_collections_counter.py) |
| 014 | [Compare The Triplets](https://www.hackerrank.com/challenges/compare-the-triplets/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign) | [014_compare_the_triplets.py](hackerrank/014_compare_the_triplets.py) |
| 015 | Compress The String | [015_compress_the_string.py](hackerrank/015_compress_the_string.py) |
| 016 | [Designer Door Mat](https://www.hackerrank.com/challenges/designer-door-mat/problem) | [016_designer_door_mat.py](hackerrank/016_designer_door_mat.py) |
| 017 | [Detect Floating Point Number](https://www.hackerrank.com/challenges/introduction-to-regex/problem) | [017_detect_floating_point_number.py](hackerrank/017_detect_floating_point_number.py) |
| 018 | [Exceptions](https://www.hackerrank.com/challenges/exceptions/problem?) | [018_exceptions.py](hackerrank/018_exceptions.py) |
| 019 | [Find A String](https://www.hackerrank.com/challenges/find-a-string/problem) | [019_find_a_string.py](hackerrank/019_find_a_string.py) |
| 020 | [Find Angle](https://www.hackerrank.com/challenges/find-angle/problem) | [020_find_angle.py](hackerrank/020_find_angle.py) |
| 021 | [Find Second Maximum Number In A List](https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem) | [021_find_second_maximum_number_in_a_list.py](hackerrank/021_find_second_maximum_number_in_a_list.py) |
| 022 | [Finding The Percentage](https://www.hackerrank.com/challenges/finding-the-percentage/problem) | [022_finding_the_percentage.py](hackerrank/022_finding_the_percentage.py) |
| 023 | Funny String | [023_funny_string.py](hackerrank/023_funny_string.py) |
| 024 | Game Of Thrones I | [024_game_of_thrones_i.py](hackerrank/024_game_of_thrones_i.py) |
| 025 | Gemstones | [025_gemstones.py](hackerrank/025_gemstones.py) |
| 026 | [Ginorts](https://www.hackerrank.com/challenges/ginorts/problem) | [026_ginorts.py](hackerrank/026_ginorts.py) |
| 027 | Hackerrank In A String | [027_hackerrank_in_a_string.py](hackerrank/027_hackerrank_in_a_string.py) |
| 028 | [Hex Color Code](https://www.hackerrank.com/challenges/hex-color-code/problem) | [028_hex_color_code.py](hackerrank/028_hex_color_code.py) |
| 029 | Highest Value Palindrome | [029_highest_value_palindrome.py](hackerrank/029_highest_value_palindrome.py) |
| 030 | Camelcase | [030_camelcase.py](hackerrank/030_camelcase.py) |
| 031 | Mars Exploration | [031_mars_exploration.py](hackerrank/031_mars_exploration.py) |
| 032 | Input Function | [032_input_function.py](hackerrank/032_input_function.py) |
| 033 | Itertools Combinations | [033_itertools_combinations.py](hackerrank/033_itertools_combinations.py) |
| 034 | Itertools Combinations With Replacement | [034_itertools_combinations_with_replacement.py](hackerrank/034_itertools_combinations_with_replacement.py) |
| 035 | [Itertools Permutations](https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=false) | [035_itertools_permutations.py](hackerrank/035_itertools_permutations.py) |
| 036 | [Itertools Product](https://www.hackerrank.com/challenges/itertools-product/problem) | [036_itertools_product.py](hackerrank/036_itertools_product.py) |
| 037 | [List Comprehensions](https://www.hackerrank.com/challenges/list-comprehensions/problem) | [037_list_comprehensions.py](hackerrank/037_list_comprehensions.py) |
| 038 | Making Anagrams | [038_making_anagrams.py](hackerrank/038_making_anagrams.py) |
| 039 | [Matching Specific String](https://www.hackerrank.com/challenges/matching-specific-string/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign) | [039_matching_specific_string.py](hackerrank/039_matching_specific_string.py) |
| 040 | [Merge The Tools](https://www.hackerrank.com/challenges/merge-the-tools/) | [040_merge_the_tools.py](hackerrank/040_merge_the_tools.py) |
| 041 | [Most Commons](https://www.hackerrank.com/challenges/most-commons/problem) | [041_most_commons.py](hackerrank/041_most_commons.py) |
| 042 | [Nested List](https://www.hackerrank.com/challenges/nested-list/problem) | [042_nested_list.py](hackerrank/042_nested_list.py) |
| 043 | Palindrome Index | [043_palindrome_index.py](hackerrank/043_palindrome_index.py) |
| 044 | Pangrams | [044_pangrams.py](hackerrank/044_pangrams.py) |
| 045 | [Piling Up](https://www.hackerrank.com/challenges/piling-up/problem) | [045_piling_up.py](hackerrank/045_piling_up.py) |
| 046 | [Polar Coordinates](https://www.hackerrank.com/challenges/polar-coordinates/problem) | [046_polar_coordinates.py](hackerrank/046_polar_coordinates.py) |
| 047 | [Print The Elements Of A Linked List](https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem) | [047_print_the_elements_of_a_linked_list.py](hackerrank/047_print_the_elements_of_a_linked_list.py) |
| 048 | [Py Collections Deque](https://www.hackerrank.com/challenges/py-collections-deque/problem) | [048_py_collections_deque.py](hackerrank/048_py_collections_deque.py) |
| 049 | [Py Collections Namedtuple](https://www.hackerrank.com/challenges/py-collections-namedtuple/problem) | [049_py_collections_namedtuple.py](hackerrank/049_py_collections_namedtuple.py) |
| 050 | [Py Collections Ordereddict](https://www.hackerrank.com/challenges/py-collections-ordereddict/problem) | [050_py_collections_ordereddict.py](hackerrank/050_py_collections_ordereddict.py) |
| 051 | [Py Hello World](https://www.hackerrank.com/challenges/py-hello-world/problem) | [051_py_hello_world.py](hackerrank/051_py_hello_world.py) |
| 052 | [Py If Else](https://www.hackerrank.com/challenges/py-if-else/problem) | [052_py_if_else.py](hackerrank/052_py_if_else.py) |
| 053 | [Py Introduction To Sets](https://www.hackerrank.com/challenges/py-introduction-to-sets/problem) | [053_py_introduction_to_sets.py](hackerrank/053_py_introduction_to_sets.py) |
| 054 | [Python Arithmetic Operators](https://www.hackerrank.com/challenges/python-arithmetic-operators/problem) | [054_python_arithmetic_operators.py](hackerrank/054_python_arithmetic_operators.py) |
| 055 | [Python Division](https://www.hackerrank.com/challenges/python-division/problem) | [055_python_division.py](hackerrank/055_python_division.py) |
| 056 | Python Evaluation | [056_python_evaluation.py](hackerrank/056_python_evaluation.py) |
| 057 | [Python Integers Come In All Sizes](https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem) | [057_python_integers_come_in_all_sizes.py](hackerrank/057_python_integers_come_in_all_sizes.py) |
| 058 | [Python Lists](https://www.hackerrank.com/challenges/python-lists/problem) | [058_python_lists.py](hackerrank/058_python_lists.py) |
| 059 | [Python Loops](https://www.hackerrank.com/challenges/python-loops/problem) | [059_python_loops.py](hackerrank/059_python_loops.py) |
| 060 | [Python Mod Divmod](https://www.hackerrank.com/challenges/python-mod-divmod/problem) | [060_python_mod_divmod.py](hackerrank/060_python_mod_divmod.py) |
| 061 | [Python Mutations](https://www.hackerrank.com/challenges/python-mutations/problem) | [061_python_mutations.py](hackerrank/061_python_mutations.py) |
| 062 | [Python Print](https://www.hackerrank.com/challenges/python-print/problem) | [062_python_print.py](hackerrank/062_python_print.py) |
| 063 | [Python String Formatting](https://www.hackerrank.com/challenges/python-string-formatting/problem) | [063_python_string_formatting.py](hackerrank/063_python_string_formatting.py) |
| 064 | [Python Time Delta](https://www.hackerrank.com/challenges/python-time-delta/problem) | [064_python_time_delta.py](hackerrank/064_python_time_delta.py) |
| 065 | [Python Tuples](https://www.hackerrank.com/challenges/python-tuples/problem) | [065_python_tuples.py](hackerrank/065_python_tuples.py) |
| 066 | [Re Split](https://www.hackerrank.com/challenges/re-split/problem) | [066_re_split.py](hackerrank/066_re_split.py) |
| 067 | Sherlock And The Valid String | [067_sherlock_and_the_valid_string.py](hackerrank/067_sherlock_and_the_valid_string.py) |
| 068 | String Construction | [068_string_construction.py](hackerrank/068_string_construction.py) |
| 069 | [String Validators](https://www.hackerrank.com/challenges/string-validators/problem) | [069_string_validators.py](hackerrank/069_string_validators.py) |
| 070 | Super Reduced String | [070_super_reduced_string.py](hackerrank/070_super_reduced_string.py) |
| 071 | [Swap Case](https://www.hackerrank.com/challenges/swap-case/problem) | [071_swap_case.py](hackerrank/071_swap_case.py) |
| 072 | [Symmetric Difference](https://www.hackerrank.com/challenges/symmetric-difference/problem) | [072_symmetric_difference.py](hackerrank/072_symmetric_difference.py) |
| 073 | [Text Alignment](https://www.hackerrank.com/challenges/text-alignment/problem) | [073_text_alignment.py](hackerrank/073_text_alignment.py) |
| 074 | [Text Wrap](https://www.hackerrank.com/challenges/text-wrap/problem) | [074_text_wrap.py](hackerrank/074_text_wrap.py) |
| 075 | [The Captains Room](https://www.hackerrank.com/challenges/py-the-captains-room/problem) | [075_the_captains_room.py](hackerrank/075_the_captains_room.py) |
| 076 | The Love Letter Mystery | [076_the_love_letter_mystery.py](hackerrank/076_the_love_letter_mystery.py) |
| 077 | [The Minion Game](https://www.hackerrank.com/challenges/the-minion-game/problem) | [077_the_minion_game.py](hackerrank/077_the_minion_game.py) |
| 078 | [Triangle Quest 2](https://www.hackerrank.com/challenges/triangle-quest-2/problem) | [078_triangle_quest_2.py](hackerrank/078_triangle_quest_2.py) |
| 079 | Two Strings | [079_two_strings.py](hackerrank/079_two_strings.py) |
| 080 | [Validating And Parsing Email Addresses](https://www.hackerrank.com/challenges/validating-named-email-addresses/problem) | [080_validating_and_parsing_email_addresses.py](hackerrank/080_validating_and_parsing_email_addresses.py) |
| 081 | [Validating Phone Numbers](https://www.hackerrank.com/challenges/validating-the-phone-number/problem) | [081_validating_phone_numbers.py](hackerrank/081_validating_phone_numbers.py) |
| 082 | [Validating Roman Numerals](https://www.hackerrank.com/challenges/validate-a-roman-number/problem) | [082_validating_roman_numerals.py](hackerrank/082_validating_roman_numerals.py) |
| 083 | [Whats Your Name](https://www.hackerrank.com/challenges/whats-your-name/problem) | [083_whats_your_name.py](hackerrank/083_whats_your_name.py) |
| 084 | [Word Order](https://www.hackerrank.com/challenges/word-order/problem) | [084_word_order.py](hackerrank/084_word_order.py) |
| 085 | [Write A Function](https://www.hackerrank.com/challenges/write-a-function/problem) | [085_write_a_function.py](hackerrank/085_write_a_function.py) |
| 086 | [Zipped](https://www.hackerrank.com/challenges/zipped/problem) | [086_zipped.py](hackerrank/086_zipped.py) |
| 087 | [Simple Array Sum](https://www.hackerrank.com/challenges/simple-array-sum/problem?isFullScreen=true) | [087_simple_array_sum.py](hackerrank/087_simple_array_sum.py) |
| 088 | [A Very Big Sum](https://www.hackerrank.com/challenges/a-very-big-sum/problem?isFullScreen=true) | [088_a_very_big_sum.py](hackerrank/088_a_very_big_sum.py) |
| 089 | [Diagonal Difference](https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true) | [089_diagonal_difference.py](hackerrank/089_diagonal_difference.py) |
| 090 | [Plus Minus](https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true) | [090_plus_minus.py](hackerrank/090_plus_minus.py) |
| 091 | [Staircase](https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true) | [091_staircase.py](hackerrank/091_staircase.py) |
| 092 | [Mini Max Sum](https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=false) | [092_mini_max_sum.py](hackerrank/092_mini_max_sum.py) |
| 093 | [Birthday Cake Candles](https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=false) | [093_birthday_cake_candles.py](hackerrank/093_birthday_cake_candles.py) |
| 094 | [Time Conversion](https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=false) | [094_time_conversion.py](hackerrank/094_time_conversion.py) |

### CodeSignal (3 solved)

| # | Problem | Solution |
|---|---------|----------|
| 001 | [Adjacent Elements Product](https://app.codesignal.com/arcade/intro/level-2/xzKiBHjhoinnpdh6m) | [001_adjacent_elements_product.py](codesignal/001_adjacent_elements_product.py) |
| 002 | [Century From Year](https://app.codesignal.com/arcade/intro/level-1/egbueTZRRL5Mm4TXN) | [002_century_from_year.py](codesignal/002_century_from_year.py) |
| 003 | [Check Palindrome](https://app.codesignal.com/arcade/intro/level-1/s5PbmwxfECC52PWyQ) | [003_check_palindrome.py](codesignal/003_check_palindrome.py) |

### Miscellaneous (AlgoExpert & others) (14 solved)

| # | Problem | Solution |
|---|---------|----------|
| 001 | Balanced Paranthesis | [001_balanced_paranthesis.py](misc/001_balanced_paranthesis.py) |
| 002 | [Find All Palindromic Substrings](https://www.youtube.com/watch?v=AdG_3GRDUfI) | [002_find_all_palindromic_substrings.py](misc/002_find_all_palindromic_substrings.py) |
| 003 | [Find The Highest Frequency Of A Character](https://www.youtube.com/watch?v=AdG_3GRDUfI) | [003_find_the_highest_frequency_of_a_character.py](misc/003_find_the_highest_frequency_of_a_character.py) |
| 004 | [Find The Kth Largest Element](https://www.youtube.com/watch?v=AdG_3GRDUfI) | [004_find_the_kth_largest_element.py](misc/004_find_the_kth_largest_element.py) |
| 005 | Gswep Assessment | [005_gswep_assessment.py](misc/005_gswep_assessment.py) |
| 006 | Max Profit | [006_max_profit.py](misc/006_max_profit.py) |
| 007 | Python String Split And Join | [007_python_string_split_and_join.py](misc/007_python_string_split_and_join.py) |
| 008 | Two Sum | [008_two_sum.py](misc/008_two_sum.py) |
| 009 | Sorted Union | [009_sorted_union.py](misc/009_sorted_union.py) |
| 010 | Longest Lexicographically Smallest Palindrome | [010_longest_lexicographically_smallest_palindrome.py](misc/010_longest_lexicographically_smallest_palindrome.py) |
| 011 | [Sorted Squared Array](https://www.algoexpert.io/questions/sorted-squared-array) | [011_sorted_squared_array.py](misc/011_sorted_squared_array.py) |
| 012 | [Tournament Winner](https://www.algoexpert.io/questions/tournament-winner) | [012_tournament_winner.py](misc/012_tournament_winner.py) |
| 013 | [Two Number Sum](https://www.algoexpert.io/questions/two-number-sum) | [013_two_number_sum.py](misc/013_two_number_sum.py) |
| 014 | [Validate Subsequence](https://www.algoexpert.io/questions/validate-subsequence) | [014_validate_subsequence.py](misc/014_validate_subsequence.py) |

<!-- END GENERATED INDEX -->
