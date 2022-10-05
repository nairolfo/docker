from types import SimpleNamespace
from fuzzywuzzy import fuzz
from difflib import SequenceMatcher

class content_matching_service():
    """ class containing methods used to match menu content with list of products' brand names """

    def process_string_before_matching(self, str):
        return str.lower().replace(" ", "").replace("-", "")

    def get_joined_terms(self, terms_dictionary):
        joined_terms = "¦".join(list(terms_dictionary.values())) 
        return SimpleNamespace( 
            original=joined_terms,
            processed=self.process_string_before_matching(joined_terms))

    def filter_match(self, match, joined_terms, menu_row):
        is_match = True
        # Filter out matches that shorter than 3
        if match.size < 3:
            return False
        # Filter out matches that have too low similarity ratio with the input
        matching_term = self.get_matching_term(joined_terms, match)
        Token_Set_Ratio1 = fuzz.token_set_ratio(menu_row, matching_term.processed)
        Token_Set_Ratio2 = fuzz.token_set_ratio(menu_row, matching_term.original)
        print(matching_term)
        print(menu_row[match.b : match.b + match.size])
        print(Token_Set_Ratio1, Token_Set_Ratio2)
        if Token_Set_Ratio1 < 80 and Token_Set_Ratio2 < 80:
            return False
        # Todo: Filter out matches that are overlapping two words in the input (for example: "r wine" matches "pinot noir wine") 
        return is_match

    def get_matching_sequences(self, joined_terms, menu_row):        
        seq = SequenceMatcher(None, joined_terms.processed , self.process_string_before_matching(menu_row))
        matchedseq = seq.get_matching_blocks()
        return list(filter(lambda match: self.filter_match(match, joined_terms, menu_row), matchedseq))

    def get_matching_term(self, joined_terms, match):
        processed_joined_terms_pre_matching_split = joined_terms.processed[:match.a].split("¦")
        matching_term_index = len(processed_joined_terms_pre_matching_split)
        return SimpleNamespace( 
            original=joined_terms.original.split("¦")[matching_term_index - 1],
            processed=processed_joined_terms_pre_matching_split[matching_term_index-1] + joined_terms.processed[match.a:].split("¦")[0])
        
        