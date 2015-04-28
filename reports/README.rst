LD Patch Implementation Reports
===============================

Reports
+++++++
.. list-table::
    :stub-columns: 2
    :header-rows: 2

    * -  
      -  
      - `ld-patch-py`_
    * -  
      - #passed
      - 502
    * - `empty`_
      - 1
      - |passed|
    * - `add-1triple`_
      - 1
      - |passed|
    * - `add-abbr-1triple`_
      - 1
      - |passed|
    * - `addnew-1triple`_
      - 1
      - |passed|
    * - `addnew-abbr-1triple`_
      - 1
      - |passed|
    * - `delete-1triple`_
      - 1
      - |passed|
    * - `delete-abbr-1triple`_
      - 1
      - |passed|
    * - `deleteexisting-1triple`_
      - 1
      - |passed|
    * - `deleteexisting-abbr-1triple`_
      - 1
      - |passed|
    * - `bind`_
      - 1
      - |passed|
    * - `bind-abbr`_
      - 1
      - |passed|
    * - `bind-overriden`_
      - 1
      - |passed|
    * - `path-forward`_
      - 1
      - |passed|
    * - `path-backward`_
      - 1
      - |passed|
    * - `path-at`_
      - 1
      - |passed|
    * - `path-unicity`_
      - 1
      - |passed|
    * - `path-unicity-fail`_
      - 1
      - |passed|
    * - `path-filter`_
      - 1
      - |passed|
    * - `path-filter-equal`_
      - 1
      - |passed|
    * - `path-starting-with-literal`_
      - 1
      - |passed|
    * - `add-noop`_
      - 1
      - |passed|
    * - `addnew-noop-fail`_
      - 1
      - |passed|
    * - `delete-noop`_
      - 1
      - |passed|
    * - `deleteexisting-noop-fail`_
      - 1
      - |passed|
    * - `cut`_
      - 1
      - |passed|
    * - `cut-abbr`_
      - 1
      - |passed|
    * - `cut-fail`_
      - 1
      - |passed|
    * - `updatelist`_
      - 1
      - |passed|
    * - `updatelist-abbr`_
      - 1
      - |passed|
    * - `updatelist-nil`_
      - 1
      - |passed|
    * - `updatelist-ambiguous`_
      - 1
      - |passed|
    * - `updatelist-not-a-list`_
      - 1
      - |passed|
    * - `updatelist-malformed-2first`_
      - 1
      - |passed|
    * - `updatelist-malformed-2rest`_
      - 1
      - |passed|
    * - `updatelist-exceed-size`_
      - 1
      - |passed|
    * - `updatelist-exceed-size-negative`_
      - 1
      - |passed|
    * - `prefix-simple`_
      - 1
      - |passed|
    * - `prefix-override`_
      - 1
      - |passed|
    * - `bnode-fresh`_
      - 1
      - |passed|
    * - `bnode-not-deleted`_
      - 1
      - |passed|
    * - `bnode-same-id`_
      - 1
      - |passed|
    * - `spec_examples-1-2-3`_
      - 1
      - |passed|
    * - `spec_examples-4-5-6`_
      - 1
      - |passed|
    * - `spec_examples-4-7-8`_
      - 1
      - |passed|
    * - `spec_examples-4-9-10`_
      - 1
      - |passed|
    * - `spec_examples-4-11-12`_
      - 1
      - |passed|
    * - `spec_examples-4-13-14`_
      - 1
      - |passed|
    * - `spec_examples-4-15-16`_
      - 1
      - |passed|
    * - `spec_examples-4-17-18`_
      - 1
      - |passed|
    * - `spec_example24_positive`_
      - 1
      - |passed|
    * - `spec_example24_negative`_
      - 1
      - |passed|
    * - `deleteexisting_var_as_object.v`_
      - 1
      - |passed|
    * - `add_no_period`_
      - 1
      - |passed|
    * - `a_var_as_subject.v`_
      - 1
      - |passed|
    * - `d_var_as_object.v`_
      - 1
      - |passed|
    * - `a_var_as_object.v`_
      - 1
      - |passed|
    * - `add_var_as_predicate`_
      - 1
      - |passed|
    * - `an_var_as_predicate.v`_
      - 1
      - |passed|
    * - `bind_no_path`_
      - 1
      - |passed|
    * - `ul_no_predicate.v`_
      - 1
      - |passed|
    * - `delete_empty_graph.v`_
      - 1
      - |passed|
    * - `d_empty_graph.v`_
      - 1
      - |passed|
    * - `bind_no_period`_
      - 1
      - |passed|
    * - `add_var_as_subject`_
      - 1
      - |passed|
    * - `deleteexisting_var_as_predicate.v`_
      - 1
      - |passed|
    * - `c_simple.v`_
      - 1
      - |passed|
    * - `add_empty_graph`_
      - 1
      - |passed|
    * - `updatelist_var`_
      - 1
      - |passed|
    * - `path_mixed`_
      - 1
      - |passed|
    * - `updatelist_literal`_
      - 1
      - |passed|
    * - `ul_iri.v`_
      - 1
      - |passed|
    * - `deleteexisting_no_period.v`_
      - 1
      - |passed|
    * - `cut_simple`_
      - 1
      - |passed|
    * - `delete_var_as_subject.v`_
      - 1
      - |passed|
    * - `an_var_as_object.v`_
      - 1
      - |passed|
    * - `bind_no_var`_
      - 1
      - |passed|
    * - `c_iri.v`_
      - 1
      - |passed|
    * - `deleteexisting_var_as_subject.v`_
      - 1
      - |passed|
    * - `deleteexisting_empty_graph.v`_
      - 1
      - |passed|
    * - `delete_no_period.v`_
      - 1
      - |passed|
    * - `de_no_period.v`_
      - 1
      - |passed|
    * - `ul_var.v`_
      - 1
      - |passed|
    * - `addnew_no_period.v`_
      - 1
      - |passed|
    * - `c_bnode.v`_
      - 1
      - |passed|
    * - `updatelist_single_index`_
      - 1
      - |passed|
    * - `de_var_as_predicate.v`_
      - 1
      - |passed|
    * - `cut_iri`_
      - 1
      - |passed|
    * - `updatelist_no_slice`_
      - 1
      - |passed|
    * - `de_var_as_object.v`_
      - 1
      - |passed|
    * - `updatelist_bnode`_
      - 1
      - |passed|
    * - `ul_bnode.v`_
      - 1
      - |passed|
    * - `empty_patch_comments`_
      - 1
      - |passed|
    * - `bind_var_unicode`_
      - 1
      - |passed|
    * - `updatelist_no_predicate`_
      - 1
      - |passed|
    * - `de_empty_graph.v`_
      - 1
      - |passed|
    * - `ul_no_value.v`_
      - 1
      - |passed|
    * - `empty_patch`_
      - 1
      - |passed|
    * - `empty_patch_whitespace`_
      - 1
      - |passed|
    * - `cut_bnode`_
      - 1
      - |passed|
    * - `an_var_as_subject.v`_
      - 1
      - |passed|
    * - `ul_literal.v`_
      - 1
      - |passed|
    * - `a_no_period.v`_
      - 1
      - |passed|
    * - `addnew_var_as_object.v`_
      - 1
      - |passed|
    * - `c_no_period.v`_
      - 1
      - |passed|
    * - `an_no_period.v`_
      - 1
      - |passed|
    * - `delete_var_as_object.v`_
      - 1
      - |passed|
    * - `de_var_as_subject.v`_
      - 1
      - |passed|
    * - `updatelist_no_period`_
      - 1
      - |passed|
    * - `ul_slice_wrong_order.v`_
      - 1
      - |passed|
    * - `updatelist_no_value`_
      - 1
      - |passed|
    * - `d_var_as_predicate.v`_
      - 1
      - |passed|
    * - `addnew_empty_graph.v`_
      - 1
      - |passed|
    * - `an_empty_graph.v`_
      - 1
      - |passed|
    * - `ul_single_index.v`_
      - 1
      - |passed|
    * - `a_empty_graph.v`_
      - 1
      - |passed|
    * - `undeclared_prefix`_
      - 1
      - |passed|
    * - `a_var_as_predicate.v`_
      - 1
      - |passed|
    * - `cut_no_period`_
      - 1
      - |passed|
    * - `updatelist_slice_wrong_order`_
      - 1
      - |passed|
    * - `d_no_period.v`_
      - 1
      - |passed|
    * - `ul_no_slice.v`_
      - 1
      - |passed|
    * - `unbound_variable`_
      - 1
      - |passed|
    * - `addnew_var_as_predicate.v`_
      - 1
      - |passed|
    * - `d_var_as_subject.v`_
      - 1
      - |passed|
    * - `add_var_as_object`_
      - 1
      - |passed|
    * - `updatelist_iri`_
      - 1
      - |passed|
    * - `ul_no_period.v`_
      - 1
      - |passed|
    * - `delete_var_as_predicate.v`_
      - 1
      - |passed|
    * - `addnew_var_as_subject.v`_
      - 1
      - |passed|
    * - `IRI_subject`_
      - 1
      - |passed|
    * - `IRI_subject__reverted`_
      - 1
      - |passed|
    * - `IRI_with_four_digit_numeric_escape`_
      - 1
      - |passed|
    * - `IRI_with_four_digit_numeric_escape__reverted`_
      - 1
      - |passed|
    * - `IRI_with_eight_digit_numeric_escape`_
      - 1
      - |passed|
    * - `IRI_with_eight_digit_numeric_escape__reverted`_
      - 1
      - |passed|
    * - `IRI_with_all_punctuation`_
      - 1
      - |passed|
    * - `IRI_with_all_punctuation__reverted`_
      - 1
      - |passed|
    * - `bareword_a_predicate`_
      - 1
      - |passed|
    * - `bareword_a_predicate__reverted`_
      - 1
      - |passed|
    * - `old_style_prefix`_
      - 1
      - |passed|
    * - `old_style_prefix__reverted`_
      - 1
      - |passed|
    * - `prefixed_IRI_predicate`_
      - 1
      - |passed|
    * - `prefixed_IRI_predicate__reverted`_
      - 1
      - |passed|
    * - `prefixed_IRI_object`_
      - 1
      - |passed|
    * - `prefixed_IRI_object__reverted`_
      - 1
      - |passed|
    * - `prefix_only_IRI`_
      - 1
      - |passed|
    * - `prefix_only_IRI__reverted`_
      - 1
      - |passed|
    * - `prefix_with_PN_CHARS_BASE_character_boundaries`_
      - 1
      - |passed|
    * - `prefix_with_PN_CHARS_BASE_character_boundaries__reverted`_
      - 1
      - |passed|
    * - `prefix_with_non_leading_extras`_
      - 1
      - |passed|
    * - `prefix_with_non_leading_extras__reverted`_
      - 1
      - |passed|
    * - `default_namespace_IRI`_
      - 1
      - |passed|
    * - `default_namespace_IRI__reverted`_
      - 1
      - |passed|
    * - `prefix_reassigned_and_used`_
      - 1
      - |passed|
    * - `prefix_reassigned_and_used__reverted`_
      - 1
      - |passed|
    * - `reserved_escaped_localName`_
      - 1
      - |passed|
    * - `reserved_escaped_localName__reverted`_
      - 1
      - |passed|
    * - `percent_escaped_localName`_
      - 1
      - |passed|
    * - `percent_escaped_localName__reverted`_
      - 1
      - |passed|
    * - `HYPHEN_MINUS_in_localName`_
      - 1
      - |passed|
    * - `HYPHEN_MINUS_in_localName__reverted`_
      - 1
      - |passed|
    * - `underscore_in_localName`_
      - 1
      - |passed|
    * - `underscore_in_localName__reverted`_
      - 1
      - |passed|
    * - `localname_with_COLON`_
      - 1
      - |passed|
    * - `localname_with_COLON__reverted`_
      - 1
      - |passed|
    * - `localName_with_assigned_nfc_bmp_PN_CHARS_BASE_character_boundaries`_
      - 1
      - |passed|
    * - `localName_with_assigned_nfc_bmp_PN_CHARS_BASE_character_boundaries__reverted`_
      - 1
      - |passed|
    * - `localName_with_assigned_nfc_PN_CHARS_BASE_character_boundaries`_
      - 0
      - |failed|
    * - `localName_with_assigned_nfc_PN_CHARS_BASE_character_boundaries__reverted`_
      - 0
      - |failed|
    * - `localName_with_nfc_PN_CHARS_BASE_character_boundaries`_
      - 1
      - |passed|
    * - `localName_with_nfc_PN_CHARS_BASE_character_boundaries__reverted`_
      - 1
      - |passed|
    * - `localName_with_leading_underscore`_
      - 1
      - |passed|
    * - `localName_with_leading_underscore__reverted`_
      - 1
      - |passed|
    * - `localName_with_leading_digit`_
      - 1
      - |passed|
    * - `localName_with_leading_digit__reverted`_
      - 1
      - |passed|
    * - `localName_with_non_leading_extras`_
      - 1
      - |passed|
    * - `localName_with_non_leading_extras__reverted`_
      - 1
      - |passed|
    * - `labeled_blank_node_subject`_
      - 1
      - |passed|
    * - `labeled_blank_node_object`_
      - 1
      - |passed|
    * - `labeled_blank_node_with_PN_CHARS_BASE_character_boundaries`_
      - 1
      - |passed|
    * - `labeled_blank_node_with_leading_underscore`_
      - 1
      - |passed|
    * - `labeled_blank_node_with_leading_digit`_
      - 1
      - |passed|
    * - `labeled_blank_node_with_non_leading_extras`_
      - 1
      - |passed|
    * - `anonymous_blank_node_subject`_
      - 1
      - |passed|
    * - `anonymous_blank_node_object`_
      - 1
      - |passed|
    * - `sole_blankNodePropertyList`_
      - 1
      - |passed|
    * - `blankNodePropertyList_as_subject`_
      - 1
      - |passed|
    * - `blankNodePropertyList_as_object`_
      - 1
      - |passed|
    * - `blankNodePropertyList_with_multiple_triples`_
      - 1
      - |passed|
    * - `nested_blankNodePropertyLists`_
      - 1
      - |passed|
    * - `blankNodePropertyList_containing_collection`_
      - 1
      - |passed|
    * - `collection_subject`_
      - 1
      - |passed|
    * - `collection_object`_
      - 1
      - |passed|
    * - `empty_collection`_
      - 1
      - |passed|
    * - `empty_collection__reverted`_
      - 1
      - |passed|
    * - `nested_collection`_
      - 1
      - |passed|
    * - `first`_
      - 1
      - |passed|
    * - `last`_
      - 1
      - |passed|
    * - `LITERAL1`_
      - 1
      - |passed|
    * - `LITERAL1__reverted`_
      - 1
      - |passed|
    * - `LITERAL1_ascii_boundaries`_
      - 1
      - |passed|
    * - `LITERAL1_ascii_boundaries__reverted`_
      - 1
      - |passed|
    * - `LITERAL1_with_UTF8_boundaries`_
      - 1
      - |passed|
    * - `LITERAL1_with_UTF8_boundaries__reverted`_
      - 1
      - |passed|
    * - `LITERAL1_all_controls`_
      - 1
      - |passed|
    * - `LITERAL1_all_controls__reverted`_
      - 1
      - |passed|
    * - `LITERAL1_all_punctuation`_
      - 1
      - |passed|
    * - `LITERAL1_all_punctuation__reverted`_
      - 1
      - |passed|
    * - `LITERAL_LONG1`_
      - 1
      - |passed|
    * - `LITERAL_LONG1__reverted`_
      - 1
      - |passed|
    * - `LITERAL_LONG1_ascii_boundaries`_
      - 1
      - |passed|
    * - `LITERAL_LONG1_ascii_boundaries__reverted`_
      - 1
      - |passed|
    * - `LITERAL_LONG1_with_UTF8_boundaries`_
      - 1
      - |passed|
    * - `LITERAL_LONG1_with_UTF8_boundaries__reverted`_
      - 1
      - |passed|
    * - `LITERAL_LONG1_with_1_squote`_
      - 1
      - |passed|
    * - `LITERAL_LONG1_with_1_squote__reverted`_
      - 1
      - |passed|
    * - `LITERAL_LONG1_with_2_squotes`_
      - 1
      - |passed|
    * - `LITERAL_LONG1_with_2_squotes__reverted`_
      - 1
      - |passed|
    * - `LITERAL2`_
      - 1
      - |passed|
    * - `LITERAL2__reverted`_
      - 1
      - |passed|
    * - `LITERAL2_ascii_boundaries`_
      - 1
      - |passed|
    * - `LITERAL2_ascii_boundaries__reverted`_
      - 1
      - |passed|
    * - `LITERAL2_with_UTF8_boundaries`_
      - 1
      - |passed|
    * - `LITERAL2_with_UTF8_boundaries__reverted`_
      - 1
      - |passed|
    * - `LITERAL_LONG2`_
      - 1
      - |passed|
    * - `LITERAL_LONG2__reverted`_
      - 1
      - |passed|
    * - `LITERAL_LONG2_ascii_boundaries`_
      - 1
      - |passed|
    * - `LITERAL_LONG2_ascii_boundaries__reverted`_
      - 1
      - |passed|
    * - `LITERAL_LONG2_with_UTF8_boundaries`_
      - 1
      - |passed|
    * - `LITERAL_LONG2_with_UTF8_boundaries__reverted`_
      - 1
      - |passed|
    * - `LITERAL_LONG2_with_1_squote`_
      - 1
      - |passed|
    * - `LITERAL_LONG2_with_1_squote__reverted`_
      - 1
      - |passed|
    * - `LITERAL_LONG2_with_2_squotes`_
      - 1
      - |passed|
    * - `LITERAL_LONG2_with_2_squotes__reverted`_
      - 1
      - |passed|
    * - `literal_with_CHARACTER_TABULATION`_
      - 1
      - |passed|
    * - `literal_with_CHARACTER_TABULATION__reverted`_
      - 1
      - |passed|
    * - `literal_with_BACKSPACE`_
      - 1
      - |passed|
    * - `literal_with_BACKSPACE__reverted`_
      - 1
      - |passed|
    * - `literal_with_LINE_FEED`_
      - 1
      - |passed|
    * - `literal_with_LINE_FEED__reverted`_
      - 1
      - |passed|
    * - `literal_with_CARRIAGE_RETURN`_
      - 1
      - |passed|
    * - `literal_with_CARRIAGE_RETURN__reverted`_
      - 1
      - |passed|
    * - `literal_with_FORM_FEED`_
      - 1
      - |passed|
    * - `literal_with_FORM_FEED__reverted`_
      - 1
      - |passed|
    * - `literal_with_REVERSE_SOLIDUS`_
      - 1
      - |passed|
    * - `literal_with_REVERSE_SOLIDUS__reverted`_
      - 1
      - |passed|
    * - `literal_with_escaped_CHARACTER_TABULATION`_
      - 1
      - |passed|
    * - `literal_with_escaped_CHARACTER_TABULATION__reverted`_
      - 1
      - |passed|
    * - `literal_with_escaped_BACKSPACE`_
      - 1
      - |passed|
    * - `literal_with_escaped_BACKSPACE__reverted`_
      - 1
      - |passed|
    * - `literal_with_escaped_LINE_FEED`_
      - 1
      - |passed|
    * - `literal_with_escaped_LINE_FEED__reverted`_
      - 1
      - |passed|
    * - `literal_with_escaped_CARRIAGE_RETURN`_
      - 1
      - |passed|
    * - `literal_with_escaped_CARRIAGE_RETURN__reverted`_
      - 1
      - |passed|
    * - `literal_with_escaped_FORM_FEED`_
      - 1
      - |passed|
    * - `literal_with_escaped_FORM_FEED__reverted`_
      - 1
      - |passed|
    * - `literal_with_numeric_escape4`_
      - 1
      - |passed|
    * - `literal_with_numeric_escape4__reverted`_
      - 1
      - |passed|
    * - `literal_with_numeric_escape8`_
      - 1
      - |passed|
    * - `literal_with_numeric_escape8__reverted`_
      - 1
      - |passed|
    * - `IRIREF_datatype`_
      - 1
      - |passed|
    * - `IRIREF_datatype__reverted`_
      - 1
      - |passed|
    * - `prefixed_name_datatype`_
      - 1
      - |passed|
    * - `prefixed_name_datatype__reverted`_
      - 1
      - |passed|
    * - `bareword_integer`_
      - 1
      - |passed|
    * - `bareword_integer__reverted`_
      - 1
      - |passed|
    * - `bareword_decimal`_
      - 1
      - |passed|
    * - `bareword_decimal__reverted`_
      - 1
      - |passed|
    * - `bareword_double`_
      - 1
      - |passed|
    * - `bareword_double__reverted`_
      - 1
      - |passed|
    * - `double_lower_case_e`_
      - 1
      - |passed|
    * - `double_lower_case_e__reverted`_
      - 1
      - |passed|
    * - `negative_numeric`_
      - 1
      - |passed|
    * - `negative_numeric__reverted`_
      - 1
      - |passed|
    * - `positive_numeric`_
      - 1
      - |passed|
    * - `positive_numeric__reverted`_
      - 1
      - |passed|
    * - `numeric_with_leading_0`_
      - 1
      - |passed|
    * - `numeric_with_leading_0__reverted`_
      - 1
      - |passed|
    * - `literal_true`_
      - 1
      - |passed|
    * - `literal_true__reverted`_
      - 1
      - |passed|
    * - `literal_false`_
      - 1
      - |passed|
    * - `literal_false__reverted`_
      - 1
      - |passed|
    * - `langtagged_non_LONG`_
      - 1
      - |passed|
    * - `langtagged_non_LONG__reverted`_
      - 1
      - |passed|
    * - `langtagged_LONG`_
      - 1
      - |passed|
    * - `langtagged_LONG__reverted`_
      - 1
      - |passed|
    * - `lantag_with_subtag`_
      - 1
      - |passed|
    * - `lantag_with_subtag__reverted`_
      - 1
      - |passed|
    * - `objectList_with_two_objects`_
      - 1
      - |passed|
    * - `objectList_with_two_objects__reverted`_
      - 1
      - |passed|
    * - `predicateObjectList_with_two_objectLists`_
      - 1
      - |passed|
    * - `predicateObjectList_with_two_objectLists__reverted`_
      - 1
      - |passed|
    * - `repeated_semis_at_end`_
      - 1
      - |passed|
    * - `repeated_semis_at_end__reverted`_
      - 1
      - |passed|
    * - `repeated_semis_not_at_end`_
      - 1
      - |passed|
    * - `repeated_semis_not_at_end__reverted`_
      - 1
      - |passed|
    * - `comment_following_localName`_
      - 1
      - |passed|
    * - `comment_following_localName__reverted`_
      - 1
      - |passed|
    * - `number_sign_following_localName`_
      - 1
      - |passed|
    * - `number_sign_following_localName__reverted`_
      - 1
      - |passed|
    * - `comment_following_PNAME_NS`_
      - 1
      - |passed|
    * - `comment_following_PNAME_NS__reverted`_
      - 1
      - |passed|
    * - `number_sign_following_PNAME_NS`_
      - 1
      - |passed|
    * - `number_sign_following_PNAME_NS__reverted`_
      - 1
      - |passed|
    * - `LITERAL_LONG2_with_REVERSE_SOLIDUS`_
      - 1
      - |passed|
    * - `LITERAL_LONG2_with_REVERSE_SOLIDUS__reverted`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-LITERAL2_with_langtag_and_datatype`_
      - 1
      - |passed|
    * - `two_LITERAL_LONG2s`_
      - 1
      - |passed|
    * - `two_LITERAL_LONG2s__reverted`_
      - 1
      - |passed|
    * - `langtagged_LONG_with_subtag`_
      - 1
      - |passed|
    * - `langtagged_LONG_with_subtag__reverted`_
      - 1
      - |passed|
    * - `turtle-syntax-uri-01`_
      - 1
      - |passed|
    * - `turtle-syntax-uri-02`_
      - 1
      - |passed|
    * - `turtle-syntax-uri-03`_
      - 1
      - |passed|
    * - `turtle-syntax-uri-04`_
      - 1
      - |passed|
    * - `turtle-syntax-prefix-04`_
      - 1
      - |passed|
    * - `turtle-syntax-prefix-05`_
      - 1
      - |passed|
    * - `turtle-syntax-prefix-06`_
      - 1
      - |passed|
    * - `turtle-syntax-prefix-07`_
      - 1
      - |passed|
    * - `turtle-syntax-prefix-08`_
      - 1
      - |passed|
    * - `turtle-syntax-prefix-09`_
      - 1
      - |passed|
    * - `turtle-syntax-string-01`_
      - 1
      - |passed|
    * - `turtle-syntax-string-02`_
      - 1
      - |passed|
    * - `turtle-syntax-string-03`_
      - 1
      - |passed|
    * - `turtle-syntax-string-04`_
      - 1
      - |passed|
    * - `turtle-syntax-string-05`_
      - 1
      - |passed|
    * - `turtle-syntax-string-06`_
      - 1
      - |passed|
    * - `turtle-syntax-string-07`_
      - 1
      - |passed|
    * - `turtle-syntax-string-08`_
      - 1
      - |passed|
    * - `turtle-syntax-string-09`_
      - 1
      - |passed|
    * - `turtle-syntax-string-10`_
      - 1
      - |passed|
    * - `turtle-syntax-string-11`_
      - 1
      - |passed|
    * - `turtle-syntax-str-esc-01`_
      - 1
      - |passed|
    * - `turtle-syntax-str-esc-02`_
      - 1
      - |passed|
    * - `turtle-syntax-str-esc-03`_
      - 1
      - |passed|
    * - `turtle-syntax-pname-esc-01`_
      - 1
      - |passed|
    * - `turtle-syntax-pname-esc-02`_
      - 1
      - |passed|
    * - `turtle-syntax-pname-esc-03`_
      - 1
      - |passed|
    * - `turtle-syntax-bnode-01`_
      - 1
      - |passed|
    * - `turtle-syntax-bnode-02`_
      - 1
      - |passed|
    * - `turtle-syntax-bnode-03`_
      - 1
      - |passed|
    * - `turtle-syntax-bnode-04`_
      - 1
      - |passed|
    * - `turtle-syntax-bnode-05`_
      - 1
      - |passed|
    * - `turtle-syntax-bnode-06`_
      - 1
      - |passed|
    * - `turtle-syntax-bnode-07`_
      - 1
      - |passed|
    * - `turtle-syntax-bnode-08`_
      - 1
      - |passed|
    * - `turtle-syntax-bnode-09`_
      - 1
      - |passed|
    * - `turtle-syntax-bnode-10`_
      - 1
      - |passed|
    * - `turtle-syntax-number-01`_
      - 1
      - |passed|
    * - `turtle-syntax-number-02`_
      - 1
      - |passed|
    * - `turtle-syntax-number-03`_
      - 1
      - |passed|
    * - `turtle-syntax-number-04`_
      - 1
      - |passed|
    * - `turtle-syntax-number-05`_
      - 1
      - |passed|
    * - `turtle-syntax-number-06`_
      - 1
      - |passed|
    * - `turtle-syntax-number-07`_
      - 1
      - |passed|
    * - `turtle-syntax-number-08`_
      - 1
      - |passed|
    * - `turtle-syntax-number-09`_
      - 1
      - |passed|
    * - `turtle-syntax-number-10`_
      - 1
      - |passed|
    * - `turtle-syntax-number-11`_
      - 1
      - |passed|
    * - `turtle-syntax-datatypes-01`_
      - 1
      - |passed|
    * - `turtle-syntax-datatypes-02`_
      - 1
      - |passed|
    * - `turtle-syntax-kw-01`_
      - 1
      - |passed|
    * - `turtle-syntax-kw-02`_
      - 1
      - |passed|
    * - `turtle-syntax-kw-03`_
      - 1
      - |passed|
    * - `turtle-syntax-struct-01`_
      - 1
      - |passed|
    * - `turtle-syntax-struct-02`_
      - 1
      - |passed|
    * - `turtle-syntax-struct-03`_
      - 1
      - |passed|
    * - `turtle-syntax-struct-04`_
      - 1
      - |passed|
    * - `turtle-syntax-struct-05`_
      - 1
      - |passed|
    * - `turtle-syntax-lists-01`_
      - 1
      - |passed|
    * - `turtle-syntax-lists-02`_
      - 1
      - |passed|
    * - `turtle-syntax-lists-03`_
      - 1
      - |passed|
    * - `turtle-syntax-lists-04`_
      - 1
      - |passed|
    * - `turtle-syntax-lists-05`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-uri-01`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-uri-02`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-uri-03`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-uri-04`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-uri-05`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-prefix-01`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-prefix-02`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-prefix-03`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-prefix-04`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-prefix-05`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-struct-01`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-struct-02`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-struct-03`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-struct-04`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-struct-05`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-struct-06`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-struct-07`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-kw-01`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-kw-02`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-kw-03`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-kw-04`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-kw-05`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-n3-extras-01`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-n3-extras-02`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-n3-extras-03`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-n3-extras-04`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-n3-extras-05`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-n3-extras-06`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-n3-extras-07`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-n3-extras-08`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-n3-extras-09`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-n3-extras-10`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-n3-extras-11`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-n3-extras-12`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-n3-extras-13`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-struct-09`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-struct-10`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-struct-12`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-struct-13`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-struct-14`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-struct-15`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-struct-16`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-struct-17`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-lang-01`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-esc-01`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-esc-02`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-esc-03`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-esc-04`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-pname-01`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-pname-02`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-pname-03`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-string-01`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-string-02`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-string-03`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-string-04`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-string-05`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-string-06`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-string-07`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-num-01`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-num-02`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-num-03`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-num-04`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-num-05`_
      - 1
      - |passed|
    * - `turtle-eval-struct-01`_
      - 1
      - |passed|
    * - `turtle-eval-struct-01__reverted`_
      - 1
      - |passed|
    * - `turtle-eval-struct-02`_
      - 1
      - |passed|
    * - `turtle-eval-struct-02__reverted`_
      - 1
      - |passed|
    * - `turtle-subm-01`_
      - 1
      - |passed|
    * - `turtle-subm-02`_
      - 1
      - |passed|
    * - `turtle-subm-02__reverted`_
      - 1
      - |passed|
    * - `turtle-subm-03`_
      - 1
      - |passed|
    * - `turtle-subm-03__reverted`_
      - 1
      - |passed|
    * - `turtle-subm-04`_
      - 1
      - |passed|
    * - `turtle-subm-04__reverted`_
      - 1
      - |passed|
    * - `turtle-subm-05`_
      - 1
      - |passed|
    * - `turtle-subm-06`_
      - 1
      - |passed|
    * - `turtle-subm-07`_
      - 1
      - |passed|
    * - `turtle-subm-07__reverted`_
      - 1
      - |passed|
    * - `turtle-subm-08`_
      - 1
      - |passed|
    * - `turtle-subm-09`_
      - 1
      - |passed|
    * - `turtle-subm-09__reverted`_
      - 1
      - |passed|
    * - `turtle-subm-10`_
      - 1
      - |passed|
    * - `turtle-subm-11`_
      - 1
      - |passed|
    * - `turtle-subm-11__reverted`_
      - 1
      - |passed|
    * - `turtle-subm-12`_
      - 1
      - |passed|
    * - `turtle-subm-12__reverted`_
      - 1
      - |passed|
    * - `turtle-subm-13`_
      - 1
      - |passed|
    * - `turtle-subm-13__reverted`_
      - 1
      - |passed|
    * - `turtle-subm-14`_
      - 1
      - |passed|
    * - `turtle-subm-15`_
      - 1
      - |passed|
    * - `turtle-subm-15__reverted`_
      - 1
      - |passed|
    * - `turtle-subm-16`_
      - 1
      - |passed|
    * - `turtle-subm-16__reverted`_
      - 1
      - |passed|
    * - `turtle-subm-17`_
      - 1
      - |passed|
    * - `turtle-subm-17__reverted`_
      - 1
      - |passed|
    * - `turtle-subm-18`_
      - 1
      - |passed|
    * - `turtle-subm-18__reverted`_
      - 1
      - |passed|
    * - `turtle-subm-19`_
      - 1
      - |passed|
    * - `turtle-subm-19__reverted`_
      - 1
      - |passed|
    * - `turtle-subm-20`_
      - 1
      - |passed|
    * - `turtle-subm-20__reverted`_
      - 1
      - |passed|
    * - `turtle-subm-21`_
      - 1
      - |passed|
    * - `turtle-subm-21__reverted`_
      - 1
      - |passed|
    * - `turtle-subm-22`_
      - 1
      - |passed|
    * - `turtle-subm-22__reverted`_
      - 1
      - |passed|
    * - `turtle-subm-23`_
      - 1
      - |passed|
    * - `turtle-subm-23__reverted`_
      - 1
      - |passed|
    * - `turtle-subm-24`_
      - 1
      - |passed|
    * - `turtle-subm-24__reverted`_
      - 1
      - |passed|
    * - `turtle-subm-25`_
      - 1
      - |passed|
    * - `turtle-subm-25__reverted`_
      - 1
      - |passed|
    * - `turtle-subm-26`_
      - 1
      - |passed|
    * - `turtle-subm-26__reverted`_
      - 1
      - |passed|
    * - `turtle-eval-bad-01`_
      - 1
      - |passed|
    * - `turtle-eval-bad-02`_
      - 1
      - |passed|
    * - `turtle-eval-bad-03`_
      - 1
      - |passed|
    * - `turtle-eval-bad-04`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-blank-label-dot-end`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-ln-dash-start`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-ln-escape-start`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-ln-escape`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-missing-ns-dot-end`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-missing-ns-dot-start`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-ns-dot-end`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-ns-dot-start`_
      - 1
      - |passed|
    * - `turtle-syntax-bad-number-dot-in-anon`_
      - 1
      - |passed|
    * - `turtle-syntax-blank-label`_
      - 1
      - |passed|
    * - `turtle-syntax-ln-colons`_
      - 1
      - |passed|
    * - `turtle-syntax-ln-dots`_
      - 1
      - |passed|
    * - `turtle-syntax-ns-dots`_
      - 1
      - |passed|

Implementations
+++++++++++++++
.. _ld-patch-py:
.. list-table::
                    :widths: 1 7
                    :stub-columns: 1

                    * - Name
                      - `ld-patch-py`_
                    * - Description
                      - ld-patch-py is a Python processor for LD Patch, based on RDFLib
                    * - Homepage
                      - https://github.com/pchampin/ld-patch-py
                    * - Passed
                      - 502/504

Tests
+++++
.. _empty:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `empty`_
                     * - Description
                       - Empty patch
.. _add-1triple:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `add-1triple`_
                     * - Description
                       - Add statement with a single triple
.. _add-abbr-1triple:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `add-abbr-1triple`_
                     * - Description
                       - Abbreviated Add statement with a single triple
.. _addnew-1triple:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `addnew-1triple`_
                     * - Description
                       - AddNew statement with a single triple
.. _addnew-abbr-1triple:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `addnew-abbr-1triple`_
                     * - Description
                       - Abbreviated AddNew statement with a single triple
.. _delete-1triple:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `delete-1triple`_
                     * - Description
                       - Delete statement with a single triple
.. _delete-abbr-1triple:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `delete-abbr-1triple`_
                     * - Description
                       - Abbreviated Delete statement with a single triple
.. _deleteexisting-1triple:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `deleteexisting-1triple`_
                     * - Description
                       - DeleteExisting statement with a single triple
.. _deleteexisting-abbr-1triple:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `deleteexisting-abbr-1triple`_
                     * - Description
                       - Abbreviated DeleteExisting statement with a single triple
.. _bind:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `bind`_
                     * - Description
                       - Binding statement
.. _bind-abbr:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `bind-abbr`_
                     * - Description
                       - Abbreviated Bind statement
.. _bind-overriden:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `bind-overriden`_
                     * - Description
                       - Overridden Bind statement
.. _path-forward:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `path-forward`_
                     * - Description
                       - Path containing a StepForward
.. _path-backward:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `path-backward`_
                     * - Description
                       - Path containing a StepBackward
.. _path-at:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `path-at`_
                     * - Description
                       - Path containing a StepAt
.. _path-unicity:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `path-unicity`_
                     * - Description
                       - Path containing a succesful unicity constraint
.. _path-unicity-fail:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `path-unicity-fail`_
                     * - Description
                       - Path containing a failed unicity constraint
.. _path-filter:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `path-filter`_
                     * - Description
                       - Path containing a filter
.. _path-filter-equal:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `path-filter-equal`_
                     * - Description
                       - Path containing a filter with an equal sign
.. _path-starting-with-literal:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `path-starting-with-literal`_
                     * - Description
                       - Path starting with a literal
.. _add-noop:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `add-noop`_
                     * - Description
                       - Add statement with an existing triple
.. _addnew-noop-fail:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `addnew-noop-fail`_
                     * - Description
                       - AddNew statement with an existing triple, failing
.. _delete-noop:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `delete-noop`_
                     * - Description
                       - Delete statement with a non-existing triple
.. _deleteexisting-noop-fail:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `deleteexisting-noop-fail`_
                     * - Description
                       - DeleteExisting statement with a non-existing triple, failing
.. _cut:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `cut`_
                     * - Description
                       - Cut
.. _cut-abbr:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `cut-abbr`_
                     * - Description
                       - Cut abbreviated
.. _cut-fail:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `cut-fail`_
                     * - Description
                       - Cut fails if no triple is deleted.
.. _updatelist:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `updatelist`_
                     * - Description
                       - UpdateList
.. _updatelist-abbr:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `updatelist-abbr`_
                     * - Description
                       - UpdateList abbreviated
.. _updatelist-nil:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `updatelist-nil`_
                     * - Description
                       - UpdateList used on an empty list (must not impact other empty lists)
.. _updatelist-ambiguous:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `updatelist-ambiguous`_
                     * - Description
                       - UpdateList fails if its subject-predicate does not point to a single list.
.. _updatelist-not-a-list:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `updatelist-not-a-list`_
                     * - Description
                       - UpdateList fails if its subject-predicate points to a non-list.
.. _updatelist-malformed-2first:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `updatelist-malformed-2first`_
                     * - Description
                       - UpdateList fails if its subject-predicate points to malformed list (with two rdf:first).
.. _updatelist-malformed-2rest:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `updatelist-malformed-2rest`_
                     * - Description
                       - UpdateList fails if its subject-predicate points to malformed list (with two rdf:rest).
.. _updatelist-exceed-size:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `updatelist-exceed-size`_
                     * - Description
                       - UpdateList with a slice exceeding the size of the list.
.. _updatelist-exceed-size-negative:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `updatelist-exceed-size-negative`_
                     * - Description
                       - UpdateList with a slice (using a negative index) exceeding the size of the list.
.. _prefix-simple:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `prefix-simple`_
                     * - Description
                       - Simple prefix
.. _prefix-override:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `prefix-override`_
                     * - Description
                       - Overridden prefix
.. _bnode-fresh:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `bnode-fresh`_
                     * - Description
                       - A bnode in the patch generates a fresh bnode in the graph, even if the bnode-id in the patch already exisists in the graph source.
.. _bnode-not-deleted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `bnode-not-deleted`_
                     * - Description
                       - A bnode in a Delete statement does not match anything.
.. _bnode-same-id:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `bnode-same-id`_
                     * - Description
                       - A bnode id in the patch always denotes the same bnode.
.. _spec_examples-1-2-3:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `spec_examples-1-2-3`_
                     * - Description
                       - Examples #1 to #3 from the LD-Patch specification
.. _spec_examples-4-5-6:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `spec_examples-4-5-6`_
                     * - Description
                       - Examples #4 to #6 from the LD-Patch specification
.. _spec_examples-4-7-8:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `spec_examples-4-7-8`_
                     * - Description
                       - Examples #4, #7 and #8 from the LD-Patch specification
.. _spec_examples-4-9-10:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `spec_examples-4-9-10`_
                     * - Description
                       - Examples #4, #9 and #10 from the LD-Patch specification
.. _spec_examples-4-11-12:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `spec_examples-4-11-12`_
                     * - Description
                       - Examples #4, #11 and #12 from the LD-Patch specification
.. _spec_examples-4-13-14:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `spec_examples-4-13-14`_
                     * - Description
                       - Examples #4, #13 and #14 from the LD-Patch specification
.. _spec_examples-4-15-16:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `spec_examples-4-15-16`_
                     * - Description
                       - Examples #4, #15 and #16 from the LD-Patch specification
.. _spec_examples-4-17-18:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `spec_examples-4-17-18`_
                     * - Description
                       - Examples #4, #17 and #18 from the LD-Patch specification
.. _spec_example24_positive:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `spec_example24_positive`_
                     * - Description
                       - Successful binding of unambiguous bnodes in a pathological graph.
.. _spec_example24_negative:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `spec_example24_negative`_
                     * - Description
                       - Unsuccessful binding in a pathological graph.
.. _deleteexisting_var_as_object.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `deleteexisting_var_as_object.v`_
                     * - Description
                       - deleteexisting var as object.v ()
.. _add_no_period:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `add_no_period`_
                     * - Description
                       - add no period
.. _a_var_as_subject.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `a_var_as_subject.v`_
                     * - Description
                       - a var as subject.v ()
.. _d_var_as_object.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `d_var_as_object.v`_
                     * - Description
                       - d var as object.v ()
.. _a_var_as_object.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `a_var_as_object.v`_
                     * - Description
                       - a var as object.v ()
.. _add_var_as_predicate:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `add_var_as_predicate`_
                     * - Description
                       - add var as predicate
.. _an_var_as_predicate.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `an_var_as_predicate.v`_
                     * - Description
                       - an var as predicate.v ()
.. _bind_no_path:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `bind_no_path`_
                     * - Description
                       - bind no path
.. _ul_no_predicate.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `ul_no_predicate.v`_
                     * - Description
                       - ul no predicate.v ()
.. _delete_empty_graph.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `delete_empty_graph.v`_
                     * - Description
                       - delete empty graph.v ()
.. _d_empty_graph.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `d_empty_graph.v`_
                     * - Description
                       - d empty graph.v ()
.. _bind_no_period:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `bind_no_period`_
                     * - Description
                       - bind no period
.. _add_var_as_subject:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `add_var_as_subject`_
                     * - Description
                       - add var as subject
.. _deleteexisting_var_as_predicate.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `deleteexisting_var_as_predicate.v`_
                     * - Description
                       - deleteexisting var as predicate.v ()
.. _c_simple.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `c_simple.v`_
                     * - Description
                       - c simple.v ()
.. _add_empty_graph:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `add_empty_graph`_
                     * - Description
                       - add empty graph
.. _updatelist_var:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `updatelist_var`_
                     * - Description
                       - updatelist var
.. _path_mixed:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `path_mixed`_
                     * - Description
                       - path mixed
.. _updatelist_literal:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `updatelist_literal`_
                     * - Description
                       - updatelist literal
.. _ul_iri.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `ul_iri.v`_
                     * - Description
                       - ul iri.v ()
.. _deleteexisting_no_period.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `deleteexisting_no_period.v`_
                     * - Description
                       - deleteexisting no period.v ()
.. _cut_simple:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `cut_simple`_
                     * - Description
                       - cut simple
.. _delete_var_as_subject.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `delete_var_as_subject.v`_
                     * - Description
                       - delete var as subject.v ()
.. _an_var_as_object.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `an_var_as_object.v`_
                     * - Description
                       - an var as object.v ()
.. _bind_no_var:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `bind_no_var`_
                     * - Description
                       - bind no var
.. _c_iri.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `c_iri.v`_
                     * - Description
                       - c iri.v ()
.. _deleteexisting_var_as_subject.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `deleteexisting_var_as_subject.v`_
                     * - Description
                       - deleteexisting var as subject.v ()
.. _deleteexisting_empty_graph.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `deleteexisting_empty_graph.v`_
                     * - Description
                       - deleteexisting empty graph.v ()
.. _delete_no_period.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `delete_no_period.v`_
                     * - Description
                       - delete no period.v ()
.. _de_no_period.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `de_no_period.v`_
                     * - Description
                       - de no period.v ()
.. _ul_var.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `ul_var.v`_
                     * - Description
                       - ul var.v ()
.. _addnew_no_period.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `addnew_no_period.v`_
                     * - Description
                       - addnew no period.v ()
.. _c_bnode.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `c_bnode.v`_
                     * - Description
                       - c bnode.v ()
.. _updatelist_single_index:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `updatelist_single_index`_
                     * - Description
                       - updatelist single index
.. _de_var_as_predicate.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `de_var_as_predicate.v`_
                     * - Description
                       - de var as predicate.v ()
.. _cut_iri:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `cut_iri`_
                     * - Description
                       - cut iri
.. _updatelist_no_slice:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `updatelist_no_slice`_
                     * - Description
                       - updatelist no slice
.. _de_var_as_object.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `de_var_as_object.v`_
                     * - Description
                       - de var as object.v ()
.. _updatelist_bnode:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `updatelist_bnode`_
                     * - Description
                       - updatelist bnode
.. _ul_bnode.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `ul_bnode.v`_
                     * - Description
                       - ul bnode.v ()
.. _empty_patch_comments:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `empty_patch_comments`_
                     * - Description
                       - empty patch comments ()
.. _bind_var_unicode:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `bind_var_unicode`_
                     * - Description
                       - bind var unicode
.. _updatelist_no_predicate:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `updatelist_no_predicate`_
                     * - Description
                       - updatelist no predicate
.. _de_empty_graph.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `de_empty_graph.v`_
                     * - Description
                       - de empty graph.v ()
.. _ul_no_value.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `ul_no_value.v`_
                     * - Description
                       - ul no value.v ()
.. _empty_patch:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `empty_patch`_
                     * - Description
                       - empty patch
.. _empty_patch_whitespace:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `empty_patch_whitespace`_
                     * - Description
                       - empty patch whitespace
.. _cut_bnode:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `cut_bnode`_
                     * - Description
                       - cut bnode
.. _an_var_as_subject.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `an_var_as_subject.v`_
                     * - Description
                       - an var as subject.v ()
.. _ul_literal.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `ul_literal.v`_
                     * - Description
                       - ul literal.v ()
.. _a_no_period.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `a_no_period.v`_
                     * - Description
                       - a no period.v ()
.. _addnew_var_as_object.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `addnew_var_as_object.v`_
                     * - Description
                       - addnew var as object.v ()
.. _c_no_period.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `c_no_period.v`_
                     * - Description
                       - c no period.v ()
.. _an_no_period.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `an_no_period.v`_
                     * - Description
                       - an no period.v ()
.. _delete_var_as_object.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `delete_var_as_object.v`_
                     * - Description
                       - delete var as object.v ()
.. _de_var_as_subject.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `de_var_as_subject.v`_
                     * - Description
                       - de var as subject.v ()
.. _updatelist_no_period:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `updatelist_no_period`_
                     * - Description
                       - updatelist no period
.. _ul_slice_wrong_order.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `ul_slice_wrong_order.v`_
                     * - Description
                       - ul slice wrong order.v ()
.. _updatelist_no_value:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `updatelist_no_value`_
                     * - Description
                       - updatelist no value
.. _d_var_as_predicate.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `d_var_as_predicate.v`_
                     * - Description
                       - d var as predicate.v ()
.. _addnew_empty_graph.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `addnew_empty_graph.v`_
                     * - Description
                       - addnew empty graph.v ()
.. _an_empty_graph.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `an_empty_graph.v`_
                     * - Description
                       - an empty graph.v ()
.. _ul_single_index.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `ul_single_index.v`_
                     * - Description
                       - ul single index.v ()
.. _a_empty_graph.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `a_empty_graph.v`_
                     * - Description
                       - a empty graph.v ()
.. _undeclared_prefix:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `undeclared_prefix`_
                     * - Description
                       - undeclared prefix
.. _a_var_as_predicate.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `a_var_as_predicate.v`_
                     * - Description
                       - a var as predicate.v ()
.. _cut_no_period:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `cut_no_period`_
                     * - Description
                       - cut no period
.. _updatelist_slice_wrong_order:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `updatelist_slice_wrong_order`_
                     * - Description
                       - updatelist slice wrong order
.. _d_no_period.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `d_no_period.v`_
                     * - Description
                       - d no period.v ()
.. _ul_no_slice.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `ul_no_slice.v`_
                     * - Description
                       - ul no slice.v ()
.. _unbound_variable:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `unbound_variable`_
                     * - Description
                       - unbound variable
.. _addnew_var_as_predicate.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `addnew_var_as_predicate.v`_
                     * - Description
                       - addnew var as predicate.v ()
.. _d_var_as_subject.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `d_var_as_subject.v`_
                     * - Description
                       - d var as subject.v ()
.. _add_var_as_object:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `add_var_as_object`_
                     * - Description
                       - add var as object
.. _updatelist_iri:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `updatelist_iri`_
                     * - Description
                       - updatelist iri
.. _ul_no_period.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `ul_no_period.v`_
                     * - Description
                       - ul no period.v ()
.. _delete_var_as_predicate.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `delete_var_as_predicate.v`_
                     * - Description
                       - delete var as predicate.v ()
.. _addnew_var_as_subject.v:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `addnew_var_as_subject.v`_
                     * - Description
                       - addnew var as subject.v ()
.. _IRI_subject:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `IRI_subject`_
                     * - Description
                       - IRI subject
.. _IRI_subject__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `IRI_subject__reverted`_
                     * - Description
                       - IRI subject
.. _IRI_with_four_digit_numeric_escape:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `IRI_with_four_digit_numeric_escape`_
                     * - Description
                       - IRI with four digit numeric escape (\u)
.. _IRI_with_four_digit_numeric_escape__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `IRI_with_four_digit_numeric_escape__reverted`_
                     * - Description
                       - IRI with four digit numeric escape (\u)
.. _IRI_with_eight_digit_numeric_escape:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `IRI_with_eight_digit_numeric_escape`_
                     * - Description
                       - IRI with eight digit numeric escape (\U)
.. _IRI_with_eight_digit_numeric_escape__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `IRI_with_eight_digit_numeric_escape__reverted`_
                     * - Description
                       - IRI with eight digit numeric escape (\U)
.. _IRI_with_all_punctuation:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `IRI_with_all_punctuation`_
                     * - Description
                       - IRI with all punctuation
.. _IRI_with_all_punctuation__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `IRI_with_all_punctuation__reverted`_
                     * - Description
                       - IRI with all punctuation
.. _bareword_a_predicate:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `bareword_a_predicate`_
                     * - Description
                       - bareword a predicate
.. _bareword_a_predicate__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `bareword_a_predicate__reverted`_
                     * - Description
                       - bareword a predicate
.. _old_style_prefix:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `old_style_prefix`_
                     * - Description
                       - old-style prefix
.. _old_style_prefix__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `old_style_prefix__reverted`_
                     * - Description
                       - old-style prefix
.. _prefixed_IRI_predicate:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `prefixed_IRI_predicate`_
                     * - Description
                       - prefixed IRI predicate
.. _prefixed_IRI_predicate__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `prefixed_IRI_predicate__reverted`_
                     * - Description
                       - prefixed IRI predicate
.. _prefixed_IRI_object:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `prefixed_IRI_object`_
                     * - Description
                       - prefixed IRI object
.. _prefixed_IRI_object__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `prefixed_IRI_object__reverted`_
                     * - Description
                       - prefixed IRI object
.. _prefix_only_IRI:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `prefix_only_IRI`_
                     * - Description
                       - prefix-only IRI (p:)
.. _prefix_only_IRI__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `prefix_only_IRI__reverted`_
                     * - Description
                       - prefix-only IRI (p:)
.. _prefix_with_PN_CHARS_BASE_character_boundaries:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `prefix_with_PN_CHARS_BASE_character_boundaries`_
                     * - Description
                       - prefix with PN CHARS BASE character boundaries (prefix: AZazÀÖØöø...:)
.. _prefix_with_PN_CHARS_BASE_character_boundaries__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `prefix_with_PN_CHARS_BASE_character_boundaries__reverted`_
                     * - Description
                       - prefix with PN CHARS BASE character boundaries (prefix: AZazÀÖØöø...:)
.. _prefix_with_non_leading_extras:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `prefix_with_non_leading_extras`_
                     * - Description
                       - prefix with_non_leading_extras (_:a·̀ͯ‿.⁀)
.. _prefix_with_non_leading_extras__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `prefix_with_non_leading_extras__reverted`_
                     * - Description
                       - prefix with_non_leading_extras (_:a·̀ͯ‿.⁀)
.. _default_namespace_IRI:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `default_namespace_IRI`_
                     * - Description
                       - default namespace IRI (:ln)
.. _default_namespace_IRI__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `default_namespace_IRI__reverted`_
                     * - Description
                       - default namespace IRI (:ln)
.. _prefix_reassigned_and_used:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `prefix_reassigned_and_used`_
                     * - Description
                       - prefix reassigned and used
.. _prefix_reassigned_and_used__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `prefix_reassigned_and_used__reverted`_
                     * - Description
                       - prefix reassigned and used
.. _reserved_escaped_localName:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `reserved_escaped_localName`_
                     * - Description
                       - reserved-escaped local name
.. _reserved_escaped_localName__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `reserved_escaped_localName__reverted`_
                     * - Description
                       - reserved-escaped local name
.. _percent_escaped_localName:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `percent_escaped_localName`_
                     * - Description
                       - percent-escaped local name
.. _percent_escaped_localName__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `percent_escaped_localName__reverted`_
                     * - Description
                       - percent-escaped local name
.. _HYPHEN_MINUS_in_localName:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `HYPHEN_MINUS_in_localName`_
                     * - Description
                       - HYPHEN-MINUS in local name
.. _HYPHEN_MINUS_in_localName__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `HYPHEN_MINUS_in_localName__reverted`_
                     * - Description
                       - HYPHEN-MINUS in local name
.. _underscore_in_localName:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `underscore_in_localName`_
                     * - Description
                       - underscore in local name
.. _underscore_in_localName__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `underscore_in_localName__reverted`_
                     * - Description
                       - underscore in local name
.. _localname_with_COLON:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `localname_with_COLON`_
                     * - Description
                       - localname with COLON
.. _localname_with_COLON__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `localname_with_COLON__reverted`_
                     * - Description
                       - localname with COLON
.. _localName_with_assigned_nfc_bmp_PN_CHARS_BASE_character_boundaries:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `localName_with_assigned_nfc_bmp_PN_CHARS_BASE_character_boundaries`_
                     * - Description
                       - localName with assigned, NFC-normalized, basic-multilingual-plane PN CHARS BASE character boundaries (p:AZazÀÖØöø...)
.. _localName_with_assigned_nfc_bmp_PN_CHARS_BASE_character_boundaries__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `localName_with_assigned_nfc_bmp_PN_CHARS_BASE_character_boundaries__reverted`_
                     * - Description
                       - localName with assigned, NFC-normalized, basic-multilingual-plane PN CHARS BASE character boundaries (p:AZazÀÖØöø...)
.. _localName_with_assigned_nfc_PN_CHARS_BASE_character_boundaries:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `localName_with_assigned_nfc_PN_CHARS_BASE_character_boundaries`_
                     * - Description
                       - localName with assigned, NFC-normalized PN CHARS BASE character boundaries (p:AZazÀÖØöø...)
.. _localName_with_assigned_nfc_PN_CHARS_BASE_character_boundaries__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `localName_with_assigned_nfc_PN_CHARS_BASE_character_boundaries__reverted`_
                     * - Description
                       - localName with assigned, NFC-normalized PN CHARS BASE character boundaries (p:AZazÀÖØöø...)
.. _localName_with_nfc_PN_CHARS_BASE_character_boundaries:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `localName_with_nfc_PN_CHARS_BASE_character_boundaries`_
                     * - Description
                       - localName with nfc-normalize PN CHARS BASE character boundaries (p:AZazÀÖØöø...)
.. _localName_with_nfc_PN_CHARS_BASE_character_boundaries__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `localName_with_nfc_PN_CHARS_BASE_character_boundaries__reverted`_
                     * - Description
                       - localName with nfc-normalize PN CHARS BASE character boundaries (p:AZazÀÖØöø...)
.. _localName_with_leading_underscore:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `localName_with_leading_underscore`_
                     * - Description
                       - localName with leading underscore (p:_)
.. _localName_with_leading_underscore__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `localName_with_leading_underscore__reverted`_
                     * - Description
                       - localName with leading underscore (p:_)
.. _localName_with_leading_digit:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `localName_with_leading_digit`_
                     * - Description
                       - localName with leading digit (p:_)
.. _localName_with_leading_digit__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `localName_with_leading_digit__reverted`_
                     * - Description
                       - localName with leading digit (p:_)
.. _localName_with_non_leading_extras:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `localName_with_non_leading_extras`_
                     * - Description
                       - localName with_non_leading_extras (_:a·̀ͯ‿.⁀)
.. _localName_with_non_leading_extras__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `localName_with_non_leading_extras__reverted`_
                     * - Description
                       - localName with_non_leading_extras (_:a·̀ͯ‿.⁀)
.. _labeled_blank_node_subject:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `labeled_blank_node_subject`_
                     * - Description
                       - labeled blank node subject
.. _labeled_blank_node_object:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `labeled_blank_node_object`_
                     * - Description
                       - labeled blank node object
.. _labeled_blank_node_with_PN_CHARS_BASE_character_boundaries:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `labeled_blank_node_with_PN_CHARS_BASE_character_boundaries`_
                     * - Description
                       - labeled blank node with PN_CHARS_BASE character boundaries (_:AZazÀÖØöø...)
.. _labeled_blank_node_with_leading_underscore:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `labeled_blank_node_with_leading_underscore`_
                     * - Description
                       - labeled blank node with_leading_underscore (_:_)
.. _labeled_blank_node_with_leading_digit:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `labeled_blank_node_with_leading_digit`_
                     * - Description
                       - labeled blank node with_leading_digit (_:0)
.. _labeled_blank_node_with_non_leading_extras:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `labeled_blank_node_with_non_leading_extras`_
                     * - Description
                       - labeled blank node with_non_leading_extras (_:a·̀ͯ‿.⁀)
.. _anonymous_blank_node_subject:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `anonymous_blank_node_subject`_
                     * - Description
                       - anonymous blank node subject
.. _anonymous_blank_node_object:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `anonymous_blank_node_object`_
                     * - Description
                       - anonymous blank node object
.. _sole_blankNodePropertyList:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `sole_blankNodePropertyList`_
                     * - Description
                       - sole blankNodePropertyList [ <p> <o> ] .
.. _blankNodePropertyList_as_subject:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `blankNodePropertyList_as_subject`_
                     * - Description
                       - blankNodePropertyList as subject [ … ] <p> <o> .
.. _blankNodePropertyList_as_object:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `blankNodePropertyList_as_object`_
                     * - Description
                       - blankNodePropertyList as object <s> <p> [ … ] .
.. _blankNodePropertyList_with_multiple_triples:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `blankNodePropertyList_with_multiple_triples`_
                     * - Description
                       - blankNodePropertyList with multiple triples [ <s> <p> ; <s2> <p2> ]
.. _nested_blankNodePropertyLists:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `nested_blankNodePropertyLists`_
                     * - Description
                       - nested blankNodePropertyLists [ <p1> [ <p2> <o2> ] ; <p3> <o3> ]
.. _blankNodePropertyList_containing_collection:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `blankNodePropertyList_containing_collection`_
                     * - Description
                       - blankNodePropertyList containing collection [ <p1> ( … ) ]
.. _collection_subject:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `collection_subject`_
                     * - Description
                       - collection subject
.. _collection_object:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `collection_object`_
                     * - Description
                       - collection object
.. _empty_collection:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `empty_collection`_
                     * - Description
                       - empty collection ()
.. _empty_collection__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `empty_collection__reverted`_
                     * - Description
                       - empty collection ()
.. _nested_collection:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `nested_collection`_
                     * - Description
                       - nested collection (())
.. _first:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `first`_
                     * - Description
                       - first, not last, non-empty nested collection
.. _last:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `last`_
                     * - Description
                       - last, not first, non-empty nested collection
.. _LITERAL1:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL1`_
                     * - Description
                       - LITERAL1 'x'
.. _LITERAL1__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL1__reverted`_
                     * - Description
                       - LITERAL1 'x'
.. _LITERAL1_ascii_boundaries:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL1_ascii_boundaries`_
                     * - Description
                       - LITERAL1_ascii_boundaries '\x00\x09\x0b\x0c\x0e\x26\x28...'
.. _LITERAL1_ascii_boundaries__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL1_ascii_boundaries__reverted`_
                     * - Description
                       - LITERAL1_ascii_boundaries '\x00\x09\x0b\x0c\x0e\x26\x28...'
.. _LITERAL1_with_UTF8_boundaries:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL1_with_UTF8_boundaries`_
                     * - Description
                       - LITERAL1_with_UTF8_boundaries '\x80\x7ff\x800\xfff...'
.. _LITERAL1_with_UTF8_boundaries__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL1_with_UTF8_boundaries__reverted`_
                     * - Description
                       - LITERAL1_with_UTF8_boundaries '\x80\x7ff\x800\xfff...'
.. _LITERAL1_all_controls:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL1_all_controls`_
                     * - Description
                       - LITERAL1_all_controls '\x00\x01\x02\x03\x04...'
.. _LITERAL1_all_controls__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL1_all_controls__reverted`_
                     * - Description
                       - LITERAL1_all_controls '\x00\x01\x02\x03\x04...'
.. _LITERAL1_all_punctuation:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL1_all_punctuation`_
                     * - Description
                       - LITERAL1_all_punctuation '!"#$%&()...'
.. _LITERAL1_all_punctuation__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL1_all_punctuation__reverted`_
                     * - Description
                       - LITERAL1_all_punctuation '!"#$%&()...'
.. _LITERAL_LONG1:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL_LONG1`_
                     * - Description
                       - LITERAL_LONG1 '''x'''
.. _LITERAL_LONG1__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL_LONG1__reverted`_
                     * - Description
                       - LITERAL_LONG1 '''x'''
.. _LITERAL_LONG1_ascii_boundaries:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL_LONG1_ascii_boundaries`_
                     * - Description
                       - LITERAL_LONG1_ascii_boundaries '\x00\x26\x28...'
.. _LITERAL_LONG1_ascii_boundaries__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL_LONG1_ascii_boundaries__reverted`_
                     * - Description
                       - LITERAL_LONG1_ascii_boundaries '\x00\x26\x28...'
.. _LITERAL_LONG1_with_UTF8_boundaries:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL_LONG1_with_UTF8_boundaries`_
                     * - Description
                       - LITERAL_LONG1_with_UTF8_boundaries '\x80\x7ff\x800\xfff...'
.. _LITERAL_LONG1_with_UTF8_boundaries__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL_LONG1_with_UTF8_boundaries__reverted`_
                     * - Description
                       - LITERAL_LONG1_with_UTF8_boundaries '\x80\x7ff\x800\xfff...'
.. _LITERAL_LONG1_with_1_squote:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL_LONG1_with_1_squote`_
                     * - Description
                       - LITERAL_LONG1 with 1 squote '''a'b'''
.. _LITERAL_LONG1_with_1_squote__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL_LONG1_with_1_squote__reverted`_
                     * - Description
                       - LITERAL_LONG1 with 1 squote '''a'b'''
.. _LITERAL_LONG1_with_2_squotes:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL_LONG1_with_2_squotes`_
                     * - Description
                       - LITERAL_LONG1 with 2 squotes '''a''b'''
.. _LITERAL_LONG1_with_2_squotes__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL_LONG1_with_2_squotes__reverted`_
                     * - Description
                       - LITERAL_LONG1 with 2 squotes '''a''b'''
.. _LITERAL2:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL2`_
                     * - Description
                       - LITERAL2 "x"
.. _LITERAL2__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL2__reverted`_
                     * - Description
                       - LITERAL2 "x"
.. _LITERAL2_ascii_boundaries:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL2_ascii_boundaries`_
                     * - Description
                       - LITERAL2_ascii_boundaries '\x00\x09\x0b\x0c\x0e\x21\x23...'
.. _LITERAL2_ascii_boundaries__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL2_ascii_boundaries__reverted`_
                     * - Description
                       - LITERAL2_ascii_boundaries '\x00\x09\x0b\x0c\x0e\x21\x23...'
.. _LITERAL2_with_UTF8_boundaries:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL2_with_UTF8_boundaries`_
                     * - Description
                       - LITERAL2_with_UTF8_boundaries '\x80\x7ff\x800\xfff...'
.. _LITERAL2_with_UTF8_boundaries__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL2_with_UTF8_boundaries__reverted`_
                     * - Description
                       - LITERAL2_with_UTF8_boundaries '\x80\x7ff\x800\xfff...'
.. _LITERAL_LONG2:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL_LONG2`_
                     * - Description
                       - LITERAL_LONG2 """x"""
.. _LITERAL_LONG2__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL_LONG2__reverted`_
                     * - Description
                       - LITERAL_LONG2 """x"""
.. _LITERAL_LONG2_ascii_boundaries:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL_LONG2_ascii_boundaries`_
                     * - Description
                       - LITERAL_LONG2_ascii_boundaries '\x00\x21\x23...'
.. _LITERAL_LONG2_ascii_boundaries__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL_LONG2_ascii_boundaries__reverted`_
                     * - Description
                       - LITERAL_LONG2_ascii_boundaries '\x00\x21\x23...'
.. _LITERAL_LONG2_with_UTF8_boundaries:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL_LONG2_with_UTF8_boundaries`_
                     * - Description
                       - LITERAL_LONG2_with_UTF8_boundaries '\x80\x7ff\x800\xfff...'
.. _LITERAL_LONG2_with_UTF8_boundaries__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL_LONG2_with_UTF8_boundaries__reverted`_
                     * - Description
                       - LITERAL_LONG2_with_UTF8_boundaries '\x80\x7ff\x800\xfff...'
.. _LITERAL_LONG2_with_1_squote:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL_LONG2_with_1_squote`_
                     * - Description
                       - LITERAL_LONG2 with 1 squote """a"b"""
.. _LITERAL_LONG2_with_1_squote__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL_LONG2_with_1_squote__reverted`_
                     * - Description
                       - LITERAL_LONG2 with 1 squote """a"b"""
.. _LITERAL_LONG2_with_2_squotes:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL_LONG2_with_2_squotes`_
                     * - Description
                       - LITERAL_LONG2 with 2 squotes """a""b"""
.. _LITERAL_LONG2_with_2_squotes__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL_LONG2_with_2_squotes__reverted`_
                     * - Description
                       - LITERAL_LONG2 with 2 squotes """a""b"""
.. _literal_with_CHARACTER_TABULATION:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `literal_with_CHARACTER_TABULATION`_
                     * - Description
                       - literal with CHARACTER TABULATION
.. _literal_with_CHARACTER_TABULATION__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `literal_with_CHARACTER_TABULATION__reverted`_
                     * - Description
                       - literal with CHARACTER TABULATION
.. _literal_with_BACKSPACE:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `literal_with_BACKSPACE`_
                     * - Description
                       - literal with BACKSPACE
.. _literal_with_BACKSPACE__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `literal_with_BACKSPACE__reverted`_
                     * - Description
                       - literal with BACKSPACE
.. _literal_with_LINE_FEED:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `literal_with_LINE_FEED`_
                     * - Description
                       - literal with LINE FEED
.. _literal_with_LINE_FEED__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `literal_with_LINE_FEED__reverted`_
                     * - Description
                       - literal with LINE FEED
.. _literal_with_CARRIAGE_RETURN:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `literal_with_CARRIAGE_RETURN`_
                     * - Description
                       - literal with CARRIAGE RETURN
.. _literal_with_CARRIAGE_RETURN__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `literal_with_CARRIAGE_RETURN__reverted`_
                     * - Description
                       - literal with CARRIAGE RETURN
.. _literal_with_FORM_FEED:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `literal_with_FORM_FEED`_
                     * - Description
                       - literal with FORM FEED
.. _literal_with_FORM_FEED__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `literal_with_FORM_FEED__reverted`_
                     * - Description
                       - literal with FORM FEED
.. _literal_with_REVERSE_SOLIDUS:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `literal_with_REVERSE_SOLIDUS`_
                     * - Description
                       - literal with REVERSE SOLIDUS
.. _literal_with_REVERSE_SOLIDUS__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `literal_with_REVERSE_SOLIDUS__reverted`_
                     * - Description
                       - literal with REVERSE SOLIDUS
.. _literal_with_escaped_CHARACTER_TABULATION:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `literal_with_escaped_CHARACTER_TABULATION`_
                     * - Description
                       - literal with escaped CHARACTER TABULATION
.. _literal_with_escaped_CHARACTER_TABULATION__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `literal_with_escaped_CHARACTER_TABULATION__reverted`_
                     * - Description
                       - literal with escaped CHARACTER TABULATION
.. _literal_with_escaped_BACKSPACE:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `literal_with_escaped_BACKSPACE`_
                     * - Description
                       - literal with escaped BACKSPACE
.. _literal_with_escaped_BACKSPACE__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `literal_with_escaped_BACKSPACE__reverted`_
                     * - Description
                       - literal with escaped BACKSPACE
.. _literal_with_escaped_LINE_FEED:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `literal_with_escaped_LINE_FEED`_
                     * - Description
                       - literal with escaped LINE FEED
.. _literal_with_escaped_LINE_FEED__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `literal_with_escaped_LINE_FEED__reverted`_
                     * - Description
                       - literal with escaped LINE FEED
.. _literal_with_escaped_CARRIAGE_RETURN:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `literal_with_escaped_CARRIAGE_RETURN`_
                     * - Description
                       - literal with escaped CARRIAGE RETURN
.. _literal_with_escaped_CARRIAGE_RETURN__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `literal_with_escaped_CARRIAGE_RETURN__reverted`_
                     * - Description
                       - literal with escaped CARRIAGE RETURN
.. _literal_with_escaped_FORM_FEED:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `literal_with_escaped_FORM_FEED`_
                     * - Description
                       - literal with escaped FORM FEED
.. _literal_with_escaped_FORM_FEED__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `literal_with_escaped_FORM_FEED__reverted`_
                     * - Description
                       - literal with escaped FORM FEED
.. _literal_with_numeric_escape4:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `literal_with_numeric_escape4`_
                     * - Description
                       - literal with numeric escape4 \u
.. _literal_with_numeric_escape4__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `literal_with_numeric_escape4__reverted`_
                     * - Description
                       - literal with numeric escape4 \u
.. _literal_with_numeric_escape8:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `literal_with_numeric_escape8`_
                     * - Description
                       - literal with numeric escape8 \U
.. _literal_with_numeric_escape8__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `literal_with_numeric_escape8__reverted`_
                     * - Description
                       - literal with numeric escape8 \U
.. _IRIREF_datatype:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `IRIREF_datatype`_
                     * - Description
                       - IRIREF datatype ""^^<t>
.. _IRIREF_datatype__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `IRIREF_datatype__reverted`_
                     * - Description
                       - IRIREF datatype ""^^<t>
.. _prefixed_name_datatype:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `prefixed_name_datatype`_
                     * - Description
                       - prefixed name datatype ""^^p:t
.. _prefixed_name_datatype__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `prefixed_name_datatype__reverted`_
                     * - Description
                       - prefixed name datatype ""^^p:t
.. _bareword_integer:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `bareword_integer`_
                     * - Description
                       - bareword integer
.. _bareword_integer__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `bareword_integer__reverted`_
                     * - Description
                       - bareword integer
.. _bareword_decimal:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `bareword_decimal`_
                     * - Description
                       - bareword decimal
.. _bareword_decimal__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `bareword_decimal__reverted`_
                     * - Description
                       - bareword decimal
.. _bareword_double:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `bareword_double`_
                     * - Description
                       - bareword double
.. _bareword_double__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `bareword_double__reverted`_
                     * - Description
                       - bareword double
.. _double_lower_case_e:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `double_lower_case_e`_
                     * - Description
                       - double lower case e
.. _double_lower_case_e__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `double_lower_case_e__reverted`_
                     * - Description
                       - double lower case e
.. _negative_numeric:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `negative_numeric`_
                     * - Description
                       - negative numeric
.. _negative_numeric__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `negative_numeric__reverted`_
                     * - Description
                       - negative numeric
.. _positive_numeric:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `positive_numeric`_
                     * - Description
                       - positive numeric
.. _positive_numeric__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `positive_numeric__reverted`_
                     * - Description
                       - positive numeric
.. _numeric_with_leading_0:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `numeric_with_leading_0`_
                     * - Description
                       - numeric with leading 0
.. _numeric_with_leading_0__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `numeric_with_leading_0__reverted`_
                     * - Description
                       - numeric with leading 0
.. _literal_true:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `literal_true`_
                     * - Description
                       - literal true
.. _literal_true__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `literal_true__reverted`_
                     * - Description
                       - literal true
.. _literal_false:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `literal_false`_
                     * - Description
                       - literal false
.. _literal_false__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `literal_false__reverted`_
                     * - Description
                       - literal false
.. _langtagged_non_LONG:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `langtagged_non_LONG`_
                     * - Description
                       - langtagged non-LONG "x"@en
.. _langtagged_non_LONG__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `langtagged_non_LONG__reverted`_
                     * - Description
                       - langtagged non-LONG "x"@en
.. _langtagged_LONG:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `langtagged_LONG`_
                     * - Description
                       - langtagged LONG """x"""@en
.. _langtagged_LONG__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `langtagged_LONG__reverted`_
                     * - Description
                       - langtagged LONG """x"""@en
.. _lantag_with_subtag:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `lantag_with_subtag`_
                     * - Description
                       - lantag with subtag "x"@en-us
.. _lantag_with_subtag__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `lantag_with_subtag__reverted`_
                     * - Description
                       - lantag with subtag "x"@en-us
.. _objectList_with_two_objects:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `objectList_with_two_objects`_
                     * - Description
                       - objectList with two objects … <o1>,<o2>
.. _objectList_with_two_objects__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `objectList_with_two_objects__reverted`_
                     * - Description
                       - objectList with two objects … <o1>,<o2>
.. _predicateObjectList_with_two_objectLists:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `predicateObjectList_with_two_objectLists`_
                     * - Description
                       - predicateObjectList with two objectLists … <o1>,<o2>
.. _predicateObjectList_with_two_objectLists__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `predicateObjectList_with_two_objectLists__reverted`_
                     * - Description
                       - predicateObjectList with two objectLists … <o1>,<o2>
.. _repeated_semis_at_end:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `repeated_semis_at_end`_
                     * - Description
                       - repeated semis at end <s> <p> <o> ;; <p2> <o2> .
.. _repeated_semis_at_end__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `repeated_semis_at_end__reverted`_
                     * - Description
                       - repeated semis at end <s> <p> <o> ;; <p2> <o2> .
.. _repeated_semis_not_at_end:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `repeated_semis_not_at_end`_
                     * - Description
                       - repeated semis not at end <s> <p> <o> ;;.
.. _repeated_semis_not_at_end__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `repeated_semis_not_at_end__reverted`_
                     * - Description
                       - repeated semis not at end <s> <p> <o> ;;.
.. _comment_following_localName:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `comment_following_localName`_
                     * - Description
                       - comment following localName
.. _comment_following_localName__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `comment_following_localName__reverted`_
                     * - Description
                       - comment following localName
.. _number_sign_following_localName:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `number_sign_following_localName`_
                     * - Description
                       - number sign following localName
.. _number_sign_following_localName__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `number_sign_following_localName__reverted`_
                     * - Description
                       - number sign following localName
.. _comment_following_PNAME_NS:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `comment_following_PNAME_NS`_
                     * - Description
                       - comment following PNAME_NS
.. _comment_following_PNAME_NS__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `comment_following_PNAME_NS__reverted`_
                     * - Description
                       - comment following PNAME_NS
.. _number_sign_following_PNAME_NS:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `number_sign_following_PNAME_NS`_
                     * - Description
                       - number sign following PNAME_NS
.. _number_sign_following_PNAME_NS__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `number_sign_following_PNAME_NS__reverted`_
                     * - Description
                       - number sign following PNAME_NS
.. _LITERAL_LONG2_with_REVERSE_SOLIDUS:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL_LONG2_with_REVERSE_SOLIDUS`_
                     * - Description
                       - REVERSE SOLIDUS at end of LITERAL_LONG2
.. _LITERAL_LONG2_with_REVERSE_SOLIDUS__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `LITERAL_LONG2_with_REVERSE_SOLIDUS__reverted`_
                     * - Description
                       - REVERSE SOLIDUS at end of LITERAL_LONG2
.. _turtle-syntax-bad-LITERAL2_with_langtag_and_datatype:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-LITERAL2_with_langtag_and_datatype`_
                     * - Description
                       - Bad number format (negative test)
.. _two_LITERAL_LONG2s:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `two_LITERAL_LONG2s`_
                     * - Description
                       - two LITERAL_LONG2s testing quote delimiter overrun
.. _two_LITERAL_LONG2s__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `two_LITERAL_LONG2s__reverted`_
                     * - Description
                       - two LITERAL_LONG2s testing quote delimiter overrun
.. _langtagged_LONG_with_subtag:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `langtagged_LONG_with_subtag`_
                     * - Description
                       - langtagged LONG with subtag """Cheers"""@en-UK
.. _langtagged_LONG_with_subtag__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `langtagged_LONG_with_subtag__reverted`_
                     * - Description
                       - langtagged LONG with subtag """Cheers"""@en-UK
.. _turtle-syntax-uri-01:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-uri-01`_
                     * - Description
                       - Only IRIs
.. _turtle-syntax-uri-02:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-uri-02`_
                     * - Description
                       - IRIs with Unicode escape
.. _turtle-syntax-uri-03:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-uri-03`_
                     * - Description
                       - IRIs with long Unicode escape
.. _turtle-syntax-uri-04:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-uri-04`_
                     * - Description
                       - Legal IRIs
.. _turtle-syntax-prefix-04:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-prefix-04`_
                     * - Description
                       - Empty @prefix with % escape
.. _turtle-syntax-prefix-05:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-prefix-05`_
                     * - Description
                       - @prefix with no suffix
.. _turtle-syntax-prefix-06:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-prefix-06`_
                     * - Description
                       - colon is a legal pname character
.. _turtle-syntax-prefix-07:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-prefix-07`_
                     * - Description
                       - dash is a legal pname character
.. _turtle-syntax-prefix-08:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-prefix-08`_
                     * - Description
                       - underscore is a legal pname character
.. _turtle-syntax-prefix-09:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-prefix-09`_
                     * - Description
                       - percents in pnames
.. _turtle-syntax-string-01:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-string-01`_
                     * - Description
                       - string literal
.. _turtle-syntax-string-02:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-string-02`_
                     * - Description
                       - langString literal
.. _turtle-syntax-string-03:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-string-03`_
                     * - Description
                       - langString literal with region
.. _turtle-syntax-string-04:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-string-04`_
                     * - Description
                       - squote string literal
.. _turtle-syntax-string-05:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-string-05`_
                     * - Description
                       - squote langString literal
.. _turtle-syntax-string-06:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-string-06`_
                     * - Description
                       - squote langString literal with region
.. _turtle-syntax-string-07:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-string-07`_
                     * - Description
                       - long string literal with embedded single- and double-quotes
.. _turtle-syntax-string-08:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-string-08`_
                     * - Description
                       - long string literal with embedded newline
.. _turtle-syntax-string-09:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-string-09`_
                     * - Description
                       - squote long string literal with embedded single- and double-quotes
.. _turtle-syntax-string-10:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-string-10`_
                     * - Description
                       - long langString literal with embedded newline
.. _turtle-syntax-string-11:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-string-11`_
                     * - Description
                       - squote long langString literal with embedded newline
.. _turtle-syntax-str-esc-01:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-str-esc-01`_
                     * - Description
                       - string literal with escaped newline
.. _turtle-syntax-str-esc-02:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-str-esc-02`_
                     * - Description
                       - string literal with Unicode escape
.. _turtle-syntax-str-esc-03:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-str-esc-03`_
                     * - Description
                       - string literal with long Unicode escape
.. _turtle-syntax-pname-esc-01:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-pname-esc-01`_
                     * - Description
                       - pname with back-slash escapes
.. _turtle-syntax-pname-esc-02:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-pname-esc-02`_
                     * - Description
                       - pname with back-slash escapes (2)
.. _turtle-syntax-pname-esc-03:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-pname-esc-03`_
                     * - Description
                       - pname with back-slash escapes (3)
.. _turtle-syntax-bnode-01:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bnode-01`_
                     * - Description
                       - bnode subject
.. _turtle-syntax-bnode-02:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bnode-02`_
                     * - Description
                       - bnode object
.. _turtle-syntax-bnode-03:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bnode-03`_
                     * - Description
                       - bnode property list object
.. _turtle-syntax-bnode-04:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bnode-04`_
                     * - Description
                       - bnode property list object (2)
.. _turtle-syntax-bnode-05:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bnode-05`_
                     * - Description
                       - bnode property list subject
.. _turtle-syntax-bnode-06:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bnode-06`_
                     * - Description
                       - labeled bnode subject
.. _turtle-syntax-bnode-07:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bnode-07`_
                     * - Description
                       - labeled bnode subject and object
.. _turtle-syntax-bnode-08:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bnode-08`_
                     * - Description
                       - bare bnode property list
.. _turtle-syntax-bnode-09:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bnode-09`_
                     * - Description
                       - bnode property list
.. _turtle-syntax-bnode-10:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bnode-10`_
                     * - Description
                       - mixed bnode property list and triple
.. _turtle-syntax-number-01:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-number-01`_
                     * - Description
                       - integer literal
.. _turtle-syntax-number-02:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-number-02`_
                     * - Description
                       - negative integer literal
.. _turtle-syntax-number-03:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-number-03`_
                     * - Description
                       - positive integer literal
.. _turtle-syntax-number-04:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-number-04`_
                     * - Description
                       - decimal literal
.. _turtle-syntax-number-05:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-number-05`_
                     * - Description
                       - decimal literal (no leading digits)
.. _turtle-syntax-number-06:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-number-06`_
                     * - Description
                       - negative decimal literal
.. _turtle-syntax-number-07:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-number-07`_
                     * - Description
                       - positive decimal literal
.. _turtle-syntax-number-08:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-number-08`_
                     * - Description
                       - integer literal with decimal lexical confusion
.. _turtle-syntax-number-09:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-number-09`_
                     * - Description
                       - double literal
.. _turtle-syntax-number-10:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-number-10`_
                     * - Description
                       - negative double literal
.. _turtle-syntax-number-11:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-number-11`_
                     * - Description
                       - double literal no fraction
.. _turtle-syntax-datatypes-01:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-datatypes-01`_
                     * - Description
                       - xsd:byte literal
.. _turtle-syntax-datatypes-02:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-datatypes-02`_
                     * - Description
                       - integer as xsd:string
.. _turtle-syntax-kw-01:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-kw-01`_
                     * - Description
                       - boolean literal (true)
.. _turtle-syntax-kw-02:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-kw-02`_
                     * - Description
                       - boolean literal (false)
.. _turtle-syntax-kw-03:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-kw-03`_
                     * - Description
                       - 'a' as keyword
.. _turtle-syntax-struct-01:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-struct-01`_
                     * - Description
                       - object list
.. _turtle-syntax-struct-02:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-struct-02`_
                     * - Description
                       - predicate list with object list
.. _turtle-syntax-struct-03:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-struct-03`_
                     * - Description
                       - predicate list with object list and dangling ';'
.. _turtle-syntax-struct-04:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-struct-04`_
                     * - Description
                       - predicate list with multiple ;;
.. _turtle-syntax-struct-05:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-struct-05`_
                     * - Description
                       - predicate list with multiple ;;
.. _turtle-syntax-lists-01:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-lists-01`_
                     * - Description
                       - empty list
.. _turtle-syntax-lists-02:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-lists-02`_
                     * - Description
                       - mixed list
.. _turtle-syntax-lists-03:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-lists-03`_
                     * - Description
                       - isomorphic list as subject and object
.. _turtle-syntax-lists-04:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-lists-04`_
                     * - Description
                       - lists of lists
.. _turtle-syntax-lists-05:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-lists-05`_
                     * - Description
                       - mixed lists with embedded lists
.. _turtle-syntax-bad-uri-01:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-uri-01`_
                     * - Description
                       - Bad IRI : space (negative test)
.. _turtle-syntax-bad-uri-02:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-uri-02`_
                     * - Description
                       - Bad IRI : bad escape (negative test)
.. _turtle-syntax-bad-uri-03:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-uri-03`_
                     * - Description
                       - Bad IRI : bad long escape (negative test)
.. _turtle-syntax-bad-uri-04:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-uri-04`_
                     * - Description
                       - Bad IRI : character escapes not allowed (negative test)
.. _turtle-syntax-bad-uri-05:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-uri-05`_
                     * - Description
                       - Bad IRI : character escapes not allowed (2) (negative test)
.. _turtle-syntax-bad-prefix-01:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-prefix-01`_
                     * - Description
                       - No prefix (negative test)
.. _turtle-syntax-bad-prefix-02:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-prefix-02`_
                     * - Description
                       - No prefix (2) (negative test)
.. _turtle-syntax-bad-prefix-03:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-prefix-03`_
                     * - Description
                       - @prefix without URI (negative test)
.. _turtle-syntax-bad-prefix-04:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-prefix-04`_
                     * - Description
                       - @prefix without prefix name (negative test)
.. _turtle-syntax-bad-prefix-05:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-prefix-05`_
                     * - Description
                       - @prefix without ':' (negative test)
.. _turtle-syntax-bad-struct-01:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-struct-01`_
                     * - Description
                       - Turtle is not TriG (negative test)
.. _turtle-syntax-bad-struct-02:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-struct-02`_
                     * - Description
                       - Turtle is not N3 (negative test)
.. _turtle-syntax-bad-struct-03:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-struct-03`_
                     * - Description
                       - Turtle is not NQuads (negative test)
.. _turtle-syntax-bad-struct-04:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-struct-04`_
                     * - Description
                       - Turtle does not allow literals-as-subjects (negative test)
.. _turtle-syntax-bad-struct-05:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-struct-05`_
                     * - Description
                       - Turtle does not allow literals-as-predicates (negative test)
.. _turtle-syntax-bad-struct-06:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-struct-06`_
                     * - Description
                       - Turtle does not allow bnodes-as-predicates (negative test)
.. _turtle-syntax-bad-struct-07:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-struct-07`_
                     * - Description
                       - Turtle does not allow labeled bnodes-as-predicates (negative test)
.. _turtle-syntax-bad-kw-01:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-kw-01`_
                     * - Description
                       - 'A' is not a keyword (negative test)
.. _turtle-syntax-bad-kw-02:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-kw-02`_
                     * - Description
                       - 'a' cannot be used as subject (negative test)
.. _turtle-syntax-bad-kw-03:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-kw-03`_
                     * - Description
                       - 'a' cannot be used as object (negative test)
.. _turtle-syntax-bad-kw-04:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-kw-04`_
                     * - Description
                       - 'true' cannot be used as subject (negative test)
.. _turtle-syntax-bad-kw-05:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-kw-05`_
                     * - Description
                       - 'true' cannot be used as object (negative test)
.. _turtle-syntax-bad-n3-extras-01:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-n3-extras-01`_
                     * - Description
                       - {} fomulae not in Turtle (negative test)
.. _turtle-syntax-bad-n3-extras-02:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-n3-extras-02`_
                     * - Description
                       - = is not Turtle (negative test)
.. _turtle-syntax-bad-n3-extras-03:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-n3-extras-03`_
                     * - Description
                       - N3 paths not in Turtle (negative test)
.. _turtle-syntax-bad-n3-extras-04:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-n3-extras-04`_
                     * - Description
                       - N3 paths not in Turtle (negative test)
.. _turtle-syntax-bad-n3-extras-05:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-n3-extras-05`_
                     * - Description
                       - N3 is...of not in Turtle (negative test)
.. _turtle-syntax-bad-n3-extras-06:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-n3-extras-06`_
                     * - Description
                       - N3 paths not in Turtle (negative test)
.. _turtle-syntax-bad-n3-extras-07:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-n3-extras-07`_
                     * - Description
                       - @keywords is not Turtle (negative test)
.. _turtle-syntax-bad-n3-extras-08:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-n3-extras-08`_
                     * - Description
                       - @keywords is not Turtle (negative test)
.. _turtle-syntax-bad-n3-extras-09:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-n3-extras-09`_
                     * - Description
                       - => is not Turtle (negative test)
.. _turtle-syntax-bad-n3-extras-10:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-n3-extras-10`_
                     * - Description
                       - <= is not Turtle (negative test)
.. _turtle-syntax-bad-n3-extras-11:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-n3-extras-11`_
                     * - Description
                       - @forSome is not Turtle (negative test)
.. _turtle-syntax-bad-n3-extras-12:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-n3-extras-12`_
                     * - Description
                       - @forAll is not Turtle (negative test)
.. _turtle-syntax-bad-n3-extras-13:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-n3-extras-13`_
                     * - Description
                       - @keywords is not Turtle (negative test)
.. _turtle-syntax-bad-struct-09:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-struct-09`_
                     * - Description
                       - extra '.' (negative test)
.. _turtle-syntax-bad-struct-10:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-struct-10`_
                     * - Description
                       - extra '.' (negative test)
.. _turtle-syntax-bad-struct-12:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-struct-12`_
                     * - Description
                       - subject, predicate, no object (negative test)
.. _turtle-syntax-bad-struct-13:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-struct-13`_
                     * - Description
                       - subject, predicate, no object (negative test)
.. _turtle-syntax-bad-struct-14:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-struct-14`_
                     * - Description
                       - literal as subject (negative test)
.. _turtle-syntax-bad-struct-15:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-struct-15`_
                     * - Description
                       - literal as predicate (negative test)
.. _turtle-syntax-bad-struct-16:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-struct-16`_
                     * - Description
                       - bnode as predicate (negative test)
.. _turtle-syntax-bad-struct-17:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-struct-17`_
                     * - Description
                       - labeled bnode as predicate (negative test)
.. _turtle-syntax-bad-lang-01:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-lang-01`_
                     * - Description
                       - langString with bad lang (negative test)
.. _turtle-syntax-bad-esc-01:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-esc-01`_
                     * - Description
                       - Bad string escape (negative test)
.. _turtle-syntax-bad-esc-02:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-esc-02`_
                     * - Description
                       - Bad string escape (negative test)
.. _turtle-syntax-bad-esc-03:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-esc-03`_
                     * - Description
                       - Bad string escape (negative test)
.. _turtle-syntax-bad-esc-04:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-esc-04`_
                     * - Description
                       - Bad string escape (negative test)
.. _turtle-syntax-bad-pname-01:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-pname-01`_
                     * - Description
                       - '~' must be escaped in pname (negative test)
.. _turtle-syntax-bad-pname-02:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-pname-02`_
                     * - Description
                       - Bad %-sequence in pname (negative test)
.. _turtle-syntax-bad-pname-03:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-pname-03`_
                     * - Description
                       - Bad unicode escape in pname (negative test)
.. _turtle-syntax-bad-string-01:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-string-01`_
                     * - Description
                       - mismatching string literal open/close (negative test)
.. _turtle-syntax-bad-string-02:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-string-02`_
                     * - Description
                       - mismatching string literal open/close (negative test)
.. _turtle-syntax-bad-string-03:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-string-03`_
                     * - Description
                       - mismatching string literal long/short (negative test)
.. _turtle-syntax-bad-string-04:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-string-04`_
                     * - Description
                       - mismatching long string literal open/close (negative test)
.. _turtle-syntax-bad-string-05:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-string-05`_
                     * - Description
                       - Long literal with missing end (negative test)
.. _turtle-syntax-bad-string-06:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-string-06`_
                     * - Description
                       - Long literal with extra quote (negative test)
.. _turtle-syntax-bad-string-07:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-string-07`_
                     * - Description
                       - Long literal with extra squote (negative test)
.. _turtle-syntax-bad-num-01:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-num-01`_
                     * - Description
                       - Bad number format (negative test)
.. _turtle-syntax-bad-num-02:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-num-02`_
                     * - Description
                       - Bad number format (negative test)
.. _turtle-syntax-bad-num-03:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-num-03`_
                     * - Description
                       - Bad number format (negative test)
.. _turtle-syntax-bad-num-04:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-num-04`_
                     * - Description
                       - Bad number format (negative test)
.. _turtle-syntax-bad-num-05:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-num-05`_
                     * - Description
                       - Bad number format (negative test)
.. _turtle-eval-struct-01:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-eval-struct-01`_
                     * - Description
                       - triple with IRIs
.. _turtle-eval-struct-01__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-eval-struct-01__reverted`_
                     * - Description
                       - triple with IRIs
.. _turtle-eval-struct-02:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-eval-struct-02`_
                     * - Description
                       - triple with IRIs and embedded whitespace
.. _turtle-eval-struct-02__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-eval-struct-02__reverted`_
                     * - Description
                       - triple with IRIs and embedded whitespace
.. _turtle-subm-01:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-01`_
                     * - Description
                       - Blank subject
.. _turtle-subm-02:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-02`_
                     * - Description
                       - @prefix and qnames
.. _turtle-subm-02__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-02__reverted`_
                     * - Description
                       - @prefix and qnames
.. _turtle-subm-03:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-03`_
                     * - Description
                       - , operator
.. _turtle-subm-03__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-03__reverted`_
                     * - Description
                       - , operator
.. _turtle-subm-04:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-04`_
                     * - Description
                       - ; operator
.. _turtle-subm-04__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-04__reverted`_
                     * - Description
                       - ; operator
.. _turtle-subm-05:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-05`_
                     * - Description
                       - empty [] as subject and object
.. _turtle-subm-06:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-06`_
                     * - Description
                       - non-empty [] as subject and object
.. _turtle-subm-07:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-07`_
                     * - Description
                       - 'a' as predicate
.. _turtle-subm-07__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-07__reverted`_
                     * - Description
                       - 'a' as predicate
.. _turtle-subm-08:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-08`_
                     * - Description
                       - simple collection
.. _turtle-subm-09:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-09`_
                     * - Description
                       - empty collection
.. _turtle-subm-09__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-09__reverted`_
                     * - Description
                       - empty collection
.. _turtle-subm-10:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-10`_
                     * - Description
                       - integer datatyped literal
.. _turtle-subm-11:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-11`_
                     * - Description
                       - decimal integer canonicalization
.. _turtle-subm-11__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-11__reverted`_
                     * - Description
                       - decimal integer canonicalization
.. _turtle-subm-12:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-12`_
                     * - Description
                       - - and _ in names and qnames
.. _turtle-subm-12__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-12__reverted`_
                     * - Description
                       - - and _ in names and qnames
.. _turtle-subm-13:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-13`_
                     * - Description
                       - tests for rdf:_<numbers> and other qnames starting with _
.. _turtle-subm-13__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-13__reverted`_
                     * - Description
                       - tests for rdf:_<numbers> and other qnames starting with _
.. _turtle-subm-14:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-14`_
                     * - Description
                       - bare : allowed
.. _turtle-subm-15:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-15`_
                     * - Description
                       - simple long literal
.. _turtle-subm-15__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-15__reverted`_
                     * - Description
                       - simple long literal
.. _turtle-subm-16:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-16`_
                     * - Description
                       - long literals with escapes
.. _turtle-subm-16__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-16__reverted`_
                     * - Description
                       - long literals with escapes
.. _turtle-subm-17:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-17`_
                     * - Description
                       - floating point number
.. _turtle-subm-17__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-17__reverted`_
                     * - Description
                       - floating point number
.. _turtle-subm-18:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-18`_
                     * - Description
                       - empty literals, normal and long variant
.. _turtle-subm-18__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-18__reverted`_
                     * - Description
                       - empty literals, normal and long variant
.. _turtle-subm-19:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-19`_
                     * - Description
                       - positive integer, decimal and doubles
.. _turtle-subm-19__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-19__reverted`_
                     * - Description
                       - positive integer, decimal and doubles
.. _turtle-subm-20:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-20`_
                     * - Description
                       - negative integer, decimal and doubles
.. _turtle-subm-20__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-20__reverted`_
                     * - Description
                       - negative integer, decimal and doubles
.. _turtle-subm-21:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-21`_
                     * - Description
                       - long literal ending in double quote
.. _turtle-subm-21__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-21__reverted`_
                     * - Description
                       - long literal ending in double quote
.. _turtle-subm-22:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-22`_
                     * - Description
                       - boolean literals
.. _turtle-subm-22__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-22__reverted`_
                     * - Description
                       - boolean literals
.. _turtle-subm-23:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-23`_
                     * - Description
                       - comments
.. _turtle-subm-23__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-23__reverted`_
                     * - Description
                       - comments
.. _turtle-subm-24:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-24`_
                     * - Description
                       - no final mewline
.. _turtle-subm-24__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-24__reverted`_
                     * - Description
                       - no final mewline
.. _turtle-subm-25:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-25`_
                     * - Description
                       - repeating a @prefix changes pname definition
.. _turtle-subm-25__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-25__reverted`_
                     * - Description
                       - repeating a @prefix changes pname definition
.. _turtle-subm-26:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-26`_
                     * - Description
                       - Variations on decimal canonicalization
.. _turtle-subm-26__reverted:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-subm-26__reverted`_
                     * - Description
                       - Variations on decimal canonicalization
.. _turtle-eval-bad-01:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-eval-bad-01`_
                     * - Description
                       - Bad IRI : good escape, bad charcater (negative evaluation test)
.. _turtle-eval-bad-02:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-eval-bad-02`_
                     * - Description
                       - Bad IRI : hex 3C is < (negative evaluation test)
.. _turtle-eval-bad-03:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-eval-bad-03`_
                     * - Description
                       - Bad IRI : hex 3E is  (negative evaluation test)
.. _turtle-eval-bad-04:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-eval-bad-04`_
                     * - Description
                       - Bad IRI : {abc} (negative evaluation test)
.. _turtle-syntax-bad-blank-label-dot-end:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-blank-label-dot-end`_
                     * - Description
                       - Blank node label must not end in dot
.. _turtle-syntax-bad-ln-dash-start:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-ln-dash-start`_
                     * - Description
                       - Local name must not begin with dash
.. _turtle-syntax-bad-ln-escape-start:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-ln-escape-start`_
                     * - Description
                       - Bad hex escape at start of local name
.. _turtle-syntax-bad-ln-escape:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-ln-escape`_
                     * - Description
                       - Bad hex escape in local name
.. _turtle-syntax-bad-missing-ns-dot-end:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-missing-ns-dot-end`_
                     * - Description
                       - Prefix must not end in dot (error in triple, not prefix directive like turtle-syntax-bad-ns-dot-end)
.. _turtle-syntax-bad-missing-ns-dot-start:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-missing-ns-dot-start`_
                     * - Description
                       - Prefix must not start with dot (error in triple, not prefix directive like turtle-syntax-bad-ns-dot-end)
.. _turtle-syntax-bad-ns-dot-end:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-ns-dot-end`_
                     * - Description
                       - Prefix must not end in dot
.. _turtle-syntax-bad-ns-dot-start:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-ns-dot-start`_
                     * - Description
                       - Prefix must not start with dot
.. _turtle-syntax-bad-number-dot-in-anon:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-bad-number-dot-in-anon`_
                     * - Description
                       - Dot delimeter may not appear in anonymous nodes
.. _turtle-syntax-blank-label:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-blank-label`_
                     * - Description
                       - Characters allowed in blank node labels
.. _turtle-syntax-ln-colons:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-ln-colons`_
                     * - Description
                       - Colons in pname local names
.. _turtle-syntax-ln-dots:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-ln-dots`_
                     * - Description
                       - Dots in pname local names
.. _turtle-syntax-ns-dots:
.. list-table::
                     :widths: 1 7
                     :stub-columns: 1
             
                     * - Name
                       - `turtle-syntax-ns-dots`_
                     * - Description
                       - Dots in namespace names

.. |passed| replace:: ✓

.. |failed| replace:: ✗

.. |canttell| replace:: ?

