import pymongo
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.npytr2k.mongodb.net/?retryWrites=true&w=majority")
db = client.test
db = client["Recycle"]
print(db)

mycollection = db["glass"]
print(mycollection)

# address starts with S:
myquery = {"address": {"$regex": "^w"}}

mydoc = mycollection.find(myquery)
print(mydoc)

# for x in mydoc:
#     print(x)

list_cusrsor = list(mydoc)
print("list cursor is")
print(list_cusrsor)

df = pd.DataFrame(list_cusrsor)
df.head()
df.drop('_id',axis=1,inplace=True)
print(df.shape)
print(df.head())
# df.to_csv('file1.csv')
print(df)


def _draw_as_table(df, pagesize):
    alternating_colors = [['white'] * len(df.columns), ['lightgray'] * len(df.columns)] * len(df)
    alternating_colors = alternating_colors[:len(df)]
    fig, ax = plt.subplots(figsize=pagesize)

    ax.axis('tight')

    ax.axis('off')
    the_table = ax.table(cellText=df.values,
                         rowLabels=df.index,
                         colLabels=df.columns,
                         rowColours=['lightblue'] * len(df),
                         colColours=['lightblue'] * len(df.columns),
                         cellColours=alternating_colors,
                         loc='center')
    return fig


def dataframe_to_pdf(df, filename, numpages=(1, 1), pagesize=(11, 8.5)):
    with PdfPages(filename) as pdf:
        nh, nv = numpages
        rows_per_page = len(df) // nh
        cols_per_page = len(df.columns) // nv
        for i in range(0, nh):
            for j in range(0, nv):
                page = df.iloc[(i * rows_per_page):min((i + 1) * rows_per_page, len(df)),
                       (j * cols_per_page):min((j + 1) * cols_per_page, len(df.columns))]
                fig = _draw_as_table(page, pagesize)
                if nh > 1 or nv > 1:
                    # Add a part/page number at bottom-center of page
                    fig.text(0.5, 0.5 / pagesize[0],
                             "Part-{}x{}: Page-{}".format(i + 1, j + 1, i * nv + j + 1),
                             ha='center', fontsize=8)
                pdf.savefig(fig, bbox_inches='tight')

                plt.close()





def getDatafromDataBASE(wastetype,address,filename):
    client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.npytr2k.mongodb.net/?retryWrites=true&w=majority")
    db = client.test
    db = client["Recycle"]
    print(db)

    mycollection = db[wastetype]
    print(mycollection)

    # address starts with S:
    myquery = {"address": {"$regex": "^"+address}}

    mydoc = mycollection.find(myquery)
    print(mydoc)

    # for x in mydoc:
    #     print(x)

    list_cusrsor = list(mydoc)
    print("list cursor is")
    print(list_cusrsor)

    df = pd.DataFrame(list_cusrsor)
    df.head()
    df.drop('_id', axis=1, inplace=True)
    print(df.shape)
    print(df.head())
    # df.to_csv('file1.csv')
    print(df)

    dataframe_to_pdf(df, filename+'.pdf')

    return filename



def getDatafromDataBASEALL(wastetype,address,filename):
    client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.npytr2k.mongodb.net/?retryWrites=true&w=majority")
    db = client.test
    db = client["Recycle"]
    print(db)

    mycollection = db[wastetype]
    print(mycollection)

    # address starts with S:


    mydoc = mycollection.find()
    print(mydoc)

    # for x in mydoc:
    #     print(x)

    list_cusrsor = list(mydoc)
    print("list cursor is")
    print(list_cusrsor)

    df = pd.DataFrame(list_cusrsor)
    df.head()
    df.drop('_id', axis=1, inplace=True)
    print(df.shape)
    print(df.head())
    # df.to_csv('file1.csv')
    print(df)

    dataframe_to_pdf(df, filename+'.pdf')

    return filename

#



