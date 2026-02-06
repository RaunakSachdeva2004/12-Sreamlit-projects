import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image



# image = Image.open('logo.jpg')

# st.image(image, use_column_width=True)

st.write("""
# DNA Nucleotide Count Werb App

This app counts the nucelotide compositions of query DNA!
***
""")


# input text box
st.write("""### Enter DNA Sequence""")
sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

#sequence = st.sidebar.text_area("Sequence input", sequence_input, height=250)
sequence = st.text_area("Sequence input", sequence_input, height=200)
sequence = sequence.splitlines()
sequence = sequence[1:] # Skips the sequence name (first line)
sequence = ''.join(sequence) # Concatenates list to string

st.write("""
***
""")

# Prints the input dna sequence

st.write("""   ### INPUT (DNA Query)""")
sequence


## DNA nucleotide count
st.write("""   ### OUTPUT (DNA Nucleotide Count)""")


# 1. print dictionary
st.write("""#### 1. Print Dictionary""")

def DNA_nucleotide_count(seq):
    d = dict([
        ("A", seq.count("A")),
        ("T", seq.count("T")),
        ("G", seq.count("G")),
        ("C", seq.count("C"))
    ])
    
    return d

X = DNA_nucleotide_count(sequence)

# X_label = list(X)
# X_values = list(X.values())

X

### 2. Print text
st.write("""#### 2. Print Text""")
st.write('There are  ' + str(X['A']) + ' adenine (A)')
st.write('There are  ' + str(X['T']) + ' thymine (T)')
st.write('There are  ' + str(X['G']) + ' guanine (G)')
st.write('There are  ' + str(X['C']) + ' cytosine (C)')


## 3. Display Dataframe

st.write(""" #### 3. Display Dataframe""")
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

### 4. Display Bar Chart using Altair
st.write(""" #### 4. Display Bar chart""")
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
st.write(p)