import pandas as pd
import os
import data_validation as dv

def save_registration_data(self,registration_data):
        # Path to the existing CSV file
        csv_file = 'data.csv'
        existed_record = dv.check_user_id_existance(csv_file,registration_data['email'])
        
        if  existed_record == None or (type(existed_record) == tuple and not existed_record[0]== True):
             new_df = pd.DataFrame([registration_data])
             main_df = pd.concat([existed_record[1], new_df], ignore_index=True)
             main_df.to_csv(csv_file, index=False)
        elif type(existed_record) == tuple and existed_record[0]== True:
            raise ValueError(f"Registatoin failed, the email {registration_data['email']} is already existed")