import streamlit as st

choice = st.sidebar.radio("Go To",("Sphere","About"))
if choice == "Sphere":

    st.title("Welcome To My Website")

    st.markdown("*This Website Made For Counting the Volume, Radius and Surface Area Of Sphere Ball*")

    st.header("What Do You Wanna Solve?")

    element = st.selectbox("Solve For:",("Volume","Radius","Surface Area"))

    st.subheader("Formula")

    if(element == "Volume"):
        r'''$$V = \frac{4}{3}\pi r^3$$'''
        pi = 3.1415926535
        columns = st.columns((1,1))
        with columns[0]:
            st.subheader("Input Value")
            r_volume = st.number_input("Enter The r Value For Volume:",min_value=0.0, step=0.1)
        with columns[1]:
            st.subheader("Output Value")
            V = 4/3* pi * r_volume**3
            st.markdown("Volume of Sphere is :")
            output = st.subheader(round(V,3))
        st.markdown("**Detail Information**")
        st.markdown(f""" 
                    * $\pi$ = {pi}
                    * r = {r_volume} 
                    """)
    elif(element == "Radius"):
        r'''
        $$r = \left(\frac{3V}{4 \pi} \right)^\frac{1}{3}$$
        '''
        pi = 3.1415926535
        columns = st.columns((1,1))
        with columns[0]:
            st.subheader("Input Value")
            volume_radius = st.number_input("Enter The V Value For Radius Sphere:",min_value=0.0, step=0.1)
        with columns[1]:
            st.subheader("Output Value")
            r = ((3*volume_radius)/(4*pi))**(1/3)
            st.markdown("Radius of Sphere is :")
            output = st.subheader(round(r,3))
        st.markdown("**Detail Information**")
        st.markdown(f""" 
                * $\pi$ = {pi}
                * V = {volume_radius} 
                    """)
    elif(element == "Surface Area"):
        r'''
        $$A = 4 \pi r^2$$
        '''
        pi = 3.1415926535
        columns = st.columns((1,1))
        with columns[0]:
            st.subheader("Input Value")
            surface_r = st.number_input("Enter The r Value For Surface Area Of Sphere:",min_value=0.0, step=0.1)
        with columns[1]:
            st.subheader("Output Value")
            A = 4*pi*(surface_r**2)
            st.markdown("Surface Area of Sphere is :")
            output = st.subheader(round(A,3))
        st.markdown("**Detail Information**")
        st.markdown(f""" 
                * $\pi$ = {pi}
                * r = {surface_r} 
                    """)

if choice == "About":
    st.title("About Me:")
    st.markdown("""
    My Name is Raka Julianza Hernanda Im a Data Analyst""")
    st.info("Build by Raka Julianza Hernanda")
    st.markdown("This is initial Version will be added some extra feature later TY :D")
    st.warning("Version 1.0")

