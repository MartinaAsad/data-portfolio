from datetime import datetime
import uuid
import os, shutil

def add_ingestion_date(df):
    df["ingestion_date"] = datetime.now()
    return df

def add_batch_id(df):
     df["batch_id"] = str(uuid.uuid4())
     return df
     
def add_source(df, source_name):
    df["source"]=source_name
    return df

def delete_folder(folder):
    if os.path.exists(folder):
      shutil.rmtree(folder)  # delete all the content and the folder itself
    os.makedirs(folder)  #create the empty folder
