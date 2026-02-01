import streamlit as st
import random

st.set_page_config(page_title="Be My Valentine 💖", page_icon="💘")

# Session state
if "yes" not in st.session_state:
    st.session_state.yes = False

if "no_col" not in st.session_state:
    st.session_state.no_col = random.randint(0, 2)

# CSS
st.markdown("""
<style>
.big-yes button {
    font-size: 30px !important;
    padding: 22px 44px !important;
    background-color: #ff3366 !important;
    color: white !important;
    border-radius: 18px !important;
}
.small-no button {
    font-size: 12px !important;
    padding: 5px 10px !important;
    background-color: #999 !important;
    color: white !important;
    border-radius: 8px !important;
}
</style>
""", unsafe_allow_html=True)

# UI
if not st.session_state.yes:
    st.markdown("<h1 style='text-align:center;color:#ff0066;'>✨ Isha ✨</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center;'>Will you be my Valentine? 💖</h2>", unsafe_allow_html=True)

    cols = st.columns(3)

    # YES button (center)
    with cols[1]:
        st.markdown('<div class="big-yes">', unsafe_allow_html=True)
        if st.button("YES 💕"):
            st.session_state.yes = True
        st.markdown('</div>', unsafe_allow_html=True)

    # NO button (jumps)
    with cols[st.session_state.no_col]:
        st.markdown('<div class="small-no">', unsafe_allow_html=True)
        if st.button("no"):
            st.session_state.no_col = random.randint(0, 2)
        st.markdown('</div>', unsafe_allow_html=True)

else:
    st.balloons()
    st.markdown("<h1 style='text-align:center;color:#ff0066;'>YAYYYY 🥰💞</h1>", unsafe_allow_html=True)

    st.image(
        "https://media.giphy.com/media/l4FGpPki5v2Bcd6Ss/giphy.gif",
        use_container_width=True
    )

    st.markdown("<h3 style='text-align:center;'>Best Valentine Ever 💘</h3>", unsafe_allow_html=True)

