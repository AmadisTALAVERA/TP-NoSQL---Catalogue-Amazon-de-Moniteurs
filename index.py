import streamlit as st
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client.amazon
monitors = db.produits

st.title("Catalogue :")


min_Price, max_Price = st.slider("Budget (€)", 50, 1000, (100, 200))


Brands = monitors.distinct("Brand")
selected_Brand = st.selectbox("Marque", ["Toutes"] + Brands)

min_Rating = st.slider("Note minimale", 0.0, 5.0, 4.5)

# in_stock_only = st.checkbox("Moniteurs en stock uniquement", value=True)


query = {
    "Price": {"$gte": min_Price, "$lte": max_Price},
    "Rating": {"$gte": min_Rating}
}
if selected_Brand != "Toutes":
    query["Brand"] = selected_Brand
# if in_stock_only:
#     query["stock"] = {"$gt": 0}

results = list(monitors.find(query).limit(50))

st.write(f"Résultats : {len(results)} moniteurs trouvés")

for m in results:
    st.write(f"{m['Brand']} - {m['Screen Size']} pouces - {m['Price']}€ - Note: {m['Rating']}") 