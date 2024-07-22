# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie :cup_with_straw:")
st.write("""Orders that need to be filled.""")


session = get_active_session()
my_dataframe = session.table("smoothies.public.orders") 
editable_df = st.experimental_data_editor(my_dataframe)
 
submitted = st.button('Submit')
if submitted: 
    st.success("Someone clicked the button.",icon="👍🏻")

    og_dataset = session.table("smoothies.public.orders")
    edited_dataset = session.create_dataframe(editable_df)
    og_dataset.merge(edited_dataset
                     , (og_dataset['name_on_order'] == edited_dataset['name_on_order'])
                     ,  [when_matched().update({'ORDER_FILLED': edited_dataset['ORDER_FILLED']})]
                    )
cnx = st.connection("snowflake")
session= = cnx.session()
