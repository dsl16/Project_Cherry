#mojo_df=mojo_df.dropna(subset=["title"])
#mojo_df['cln_title']=pd.DataFrame(map(lambda x: re.sub('[^a-zA-Z0-9]','',x), mojo_df["title"]))
#meta_df=mojo_df.dropna(subset=["title"])
#meta_df['cln_title']=pd.DataFrame(map(lambda x: re.sub('[^a-zA-Z0-9]','',x), meta_df["title"]))


## Bing:  reset_index fixed the title mis-alignment
mojo_df = mojo_df.dropna(subset=["title"])
mojo_df = mojo_df.reset_index(drop=True)
mojo_df['cln_title']=pd.DataFrame(map(lambda x: re.sub('[^a-zA-Z0-9]','',x), mojo_df["title"]))
meta_df = meta_df.dropna(subset=["title"])
meta_df = meta_df.reset_index(drop=True)
meta_df['cln_title']=pd.DataFrame(map(lambda x: re.sub('[^a-zA-Z0-9]','',x), meta_df["title"]))
