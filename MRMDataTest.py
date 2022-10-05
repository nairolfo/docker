import csv
import time
from mrm_data_access_layer import mrm_data_access_layer
from content_matching_service import content_matching_service

start = time.time()

# dal = mrm_data_access_layer()
# connection = dal.create_server_connection()
# dal.reset_mrm_db(connection)
#
# terms_dictionary = dal.get_terms(connection)
# match_service = content_matching_service()
# joined_terms = match_service.get_joined_terms(terms_dictionary)
line_count = 0
# with open('input.csv', encoding='utf-8') as input_file:
#     csv_reader = csv.reader(input_file, delimiter=',')
#
#     for row in csv_reader:
#         if line_count > 0:
#             menu_row = row[1] + ' ' + row[2]
#             # Here I define the line_count as the menu row unique identifier for the db,
#             # if the table were to be expanded with other input files, this would need to be changed
#             dal.insert_menu(connection, line_count, int(row[0]), row[1], row[2])
#
#             matching_sequences = match_service.get_matching_sequences(joined_terms, menu_row)
#
#             if (len(matching_sequences) > 0):
#                 for match in matching_sequences:
#                     matching_term = match_service.get_matching_term(joined_terms, match).original
#
#                     first_match_termid = list(terms_dictionary.keys())[list(terms_dictionary.values()).index(matching_term)]
#                     dal.insert_match(connection, line_count, first_match_termid)
#         line_count += 1

# connection.close();
end = time.time()     
print(f'Processed {line_count} lines in {end - start}s.')  






