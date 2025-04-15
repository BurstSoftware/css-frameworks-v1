import streamlit as st

# Framework categories and their lists
frameworks = {
    "General Purpose": [
        "Bootstrap - Extensive components and grid system",
        "Foundation - Flexible and mobile-first",
        "Bulma - Modern and Flexbox-based",
        "Semantic UI - Human-friendly HTML styling"
    ],
    "Utility-First": [
        "Tailwind CSS - Low-level utility classes",
        "Tachyons - Functional, single-purpose classes"
    ],
    "Lightweight": [
        "Pure.css - Minimalistic with a small footprint",
        "Spectre.css - Lightweight and modern",
        "Milligram - Ultra-light (~2kb)",
        "Skeleton - Simple responsive boilerplate",
        "Pico.css - Minimal with native HTML styling"
    ],
    "Component-Based": [
        "Materialize CSS - Based on Material Design",
        "UIkit - Modular with modern components",
        "Chakra UI - Accessible React components",
        "Ant Design - Robust React UI framework"
    ]
}

# Streamlit app
def main():
    # App title
    st.title("CSS Frameworks Explorer")

    # Dropdown at the top of the main app
    selected_category = st.selectbox(
        "Choose a Framework Category",
        options=list(frameworks.keys()),
        index=0  # Start with the first category
    )

    # Display the list of frameworks for the selected category
    st.subheader(f"{selected_category} Frameworks")
    for framework in frameworks[selected_category]:
        st.write(f"- {framework}")

if __name__ == "__main__":
    main()
