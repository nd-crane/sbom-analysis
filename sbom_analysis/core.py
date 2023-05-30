# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['show_metadata']

# %% ../nbs/00_core.ipynb 6
def show_metadata(kg, dataframe=True):
    """
    Return total number of triples, distict entities, and properties to a pandas dataframe.
    Print if df=false
    """
    
    query = """
    SELECT 
        (COUNT(*) as ?count)
    WHERE {
      ?s ?p ?o .
    }
    """

    if dataframe:
        return kg.query_as_df(query)
    
    result = kg.query(query)
    for row in result:
        print("Total Triples:", row["count"])

