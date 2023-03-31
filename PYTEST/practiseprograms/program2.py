from practiseprograms.program1 import searchfiles
def test_files():
    obj=searchfiles()
    data=obj.searchfiles("D://data","covid.csv")
    assert data==['D://data\\covid.csv']
