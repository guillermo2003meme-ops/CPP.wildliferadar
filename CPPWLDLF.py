# CPPWLDLF.py
import streamlit as st
import pandas as pd
import requests
import json
from PIL import Image
import os

# --- CRITICAL: st.set_page_config MUST be the very first Streamlit command ---
st.set_page_config(page_title="CPP Wildlife Radar", layout="wide", initial_sidebar_state="collapsed")

# Import bird data
from CPPWLDLFbirds import BIRD_SPECIES, BIRD_DETAILS, DEFAULT_BIRD_IMAGE

# ====================== CUSTOM IMAGES ======================
# Replace these with your own image paths or URLs.
HEADER_IMAGE = "https://www.cpp.edu/biotrek/img/wildflower_Voorhis.jpg"   # e.g., "https://example.com/header.jpg" or "images/top_banner.png"
FOOTER_IMAGE = "https://www.cpp.edu/biotrek/img/garden_bee.jpg"   # bottom image
# ============================================================

def get_bird_detail(common_name):
    """Get detailed information for a bird."""
    return BIRD_DETAILS.get(common_name, None)

def search_birds(query):
    """Search for birds by common name."""
    if not query:
        return BIRD_SPECIES
    query_lower = query.lower()
    return [b for b in BIRD_SPECIES if query_lower in b["common"].lower() or query_lower in b["scientific"].lower()]

def load_image(image_path, default_text=""):
    """Safely load an image (local or URL) or show placeholder text."""
    if os.path.isfile(image_path):
        return Image.open(image_path)
    elif image_path.startswith("http"):
        try:
            response = requests.get(image_path, stream=True, timeout=10)
            if response.status_code == 200:
                return Image.open(response.raw)
        except:
            pass
    return None

# --- Page Navigation ---
if "page" not in st.session_state:
    st.session_state.page = "home"
if "selected_bird" not in st.session_state:
    st.session_state.selected_bird = None

# --- Page Navigation ---
if "page" not in st.session_state:
    st.session_state.page = "home"
if "selected_bird" not in st.session_state:
    st.session_state.selected_bird = None


# --- PAGE: HOME ---
def render_home():
    # Hero Section with mission statements
    st.markdown("""
    <style>
    .hero-text {
        font-size: 1.1rem;
        line-height: 1.6;
        color: #2c3e50;
    }
    .mission-box {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        margin: 15px 0;
        border-left: 5px solid #2e7d32;
    }
    .category-card {
        text-align: center;
        padding: 15px;
        border-radius: 10px;
        background-color: #f0f4f0;
        transition: transform 0.3s;
        cursor: pointer;
        border: 2px solid transparent;
    }
    .category-card:hover {
        transform: scale(1.02);
        border-color: #2e7d32;
    }
    .category-card img {
        width: 100%;
        height: 150px;
        object-fit: cover;
        border-radius: 8px;
    }
    .category-card h4 {
        margin-top: 10px;
        color: #1a3c1a;
    }
    </style>
    """, unsafe_allow_html=True)

    # --- Custom Header Image ---
        # --- Custom Header Image (with max-height) ---
    # --- Custom Header Banner with overlaid title ---
    if HEADER_IMAGE:
        st.markdown(f"""
        <div style="position: relative; text-align: center; margin-bottom: 30px;">
            <img src="{HEADER_IMAGE}" alt="Header" style="width:100%; max-height:200px; object-fit: cover; object-position: center;">
            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; text-shadow: 2px 2px 4px rgba(0,0,0,0.6);">
                <h1 style="margin:0; font-size:2.5rem;">Cal Poly Pomona Wildlife Radar</h1>
                <p style="margin:5px 0 0 0; font-size:1.1rem;">Your hub for campus biodiversity data and environmental reporting</p>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.title("Cal Poly Pomona Wildlife Radar")
        st.markdown("*Your hub for campus biodiversity data and environmental reporting*")
        st.info("Header image not set. Add a URL or local path in HEADER_IMAGE.")

    # ================================================
    # Category Cards
    # ================================================
    st.markdown("---")
    st.subheader("Explore Campus Wildlife")

    categories = [
        {"name": "Birds", "image": "https://www.allaboutbirds.org/guide/assets/og/654910729-1200px.jpg", "page": "birds"},
        {"name": "Mammals", "image": "https://static.wixstatic.com/media/610241_5a1017b01f5f409c8f93daec79337142~mv2.jpg/v1/fill/w_568,h_378,al_c,q_80,usm_0.66_1.00_0.01,enc_avif,quality_auto/610241_5a1017b01f5f409c8f93daec79337142~mv2.jpg", "page": "coming_soon"},
        {"name": "Amphibians", "image": "https://upload.wikimedia.org/wikipedia/commons/0/0f/Bufo_americanus_PJC1.jpg", "page": "coming_soon"},
        {"name": "Insects", "image": "https://upload.wikimedia.org/wikipedia/commons/b/b4/Monarch_Butterfly_Danaus_plexippus_Milkweed.jpg", "page": "coming_soon"},
        {"name": "Plants", "image": "https://upload.wikimedia.org/wikipedia/commons/c/c4/Matilija_Poppy_1_%2814134391966%29.jpg", "page": "coming_soon"},
        {"name": "Fungi", "image": "https://upload.wikimedia.org/wikipedia/commons/6/62/Turkey_tail_Fungus._%2841856600312%29.jpg", "page": "coming_soon"}
    ]

    cols = st.columns(3)
    for i, category in enumerate(categories):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="category-card">
                <img src="{category['image']}" alt="{category['name']}">
                <h4>{category['name']}</h4>
            </div>
            """, unsafe_allow_html=True)
            if category["page"] == "birds":
                if st.button(f"Explore {category['name']}", key=f"btn_{category['name']}"):
                    st.session_state.page = "birds"
                    st.rerun()
            else:
                st.button(f"Coming Soon", key=f"btn_{category['name']}", disabled=True)

    # ================================================
    # Mission Statements
    # ================================================
    st.markdown("---")
    st.subheader("Our Mission")

    missions = [
        "Our platform centralizes Cal Poly Pomona's rich biodiversity data to serve as the definitive source for wildlife records, supporting long-term population tracking, historical documentation, and the monitoring of special-status species across campus.",
        "It streamlines the preparation of Environmental Assessment Reports by providing essential baseline data on species presence, helping campus planners identify potential impacts, plan mitigation strategies, and define restoration success criteria.",
        "It transforms the campus into a living laboratory, empowering students with real-world datasets for research projects, field studies, and experiential learning across disciplines from introductory biology to advanced ecology.",
        "It fuels scientific inquiry by enabling researchers to investigate critical environmental questions—such as the effects of urbanization, fire, and pollutants—while contributing data to collaborative networks like the Urban Wildlife Information Network.",
        "Ultimately, our website bridges academic research, environmental stewardship, and hands-on education, ensuring that Cal Poly Pomona's wildlife data drives informed decision-making, conservation action, and the next generation of scientific discovery."
    ]

    for mission in missions:
        st.markdown(f'<div class="mission-box"><p class="hero-text">{mission}</p></div>', unsafe_allow_html=True)

    # Campus Stats (no emoji)
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Bird Species", "100+", "Documented on campus")
    with col2:
        st.metric("Vascular Plants", "261", "Inventoried species")
    with col3:
        st.metric("Special-Status Species", "Multiple", "Including California Gnatcatcher")
    with col4:
        st.metric("Research Hours", "250+", "Field work by students & faculty")

    # --- Environmental Assessment Resources ---
    st.markdown("---")
    st.subheader("Environmental Assessment Resources")

    with st.expander("Click here to learn how to fill out the Environmental Assessment (CEQA Initial Study)", expanded=True):
        st.markdown("""
        ### What is an Environmental Assessment?
        In California, most projects on public lands (like Cal Poly Pomona) must comply with the **California Environmental Quality Act (CEQA)**.  
        An *Environmental Assessment* (often an *Initial Study*) is a document that analyzes whether a proposed project may have significant environmental impacts.

        ### How to Complete the Assessment
        1. **Describe the project** – What is being built, where, and how big?
        2. **Evaluate environmental factors** – Use the checklist to assess potential impacts on:
           - Aesthetics, air quality, biological resources (wildlife, plants), cultural resources, energy, geology, hazards, hydrology, land use, noise, population, public services, recreation, transportation, tribal resources, utilities, and wildfire.
        3. **Determine significance** – For each impact category, check:
           - No impact
           - Less than significant impact
           - Less than significant with mitigation
           - Potentially significant impact
        4. **Propose mitigation measures** – If an impact is significant, describe how it will be reduced or avoided.
        5. **Prepare the document** – Compile findings, attach any supporting studies, and circulate for public review.

        ### Campus‑Specific Considerations
        At Cal Poly Pomona, special attention must be given to:
        - **Biological resources** – The campus is home to sensitive species like the *California Gnatcatcher* and rare plants.
        - **Cultural resources** – The Voorhis Ecological Reserve and nearby archaeological sites.
        - **Wildfire risk** – The area is in a high‑fire‑hazard zone.

        For more information and to view the most recent Environmental Impact Reports, use the link below. You may need to coordinate with the campus **Office of Planning, Design & Construction** for a project‑specific EA.
        """)

        st.markdown("**Access the most recent Environmental Impact Reports**")
        st.link_button(
            "View CPP Master Plan EIR",
            "https://www.cpp.edu/fpm/pdc/master-plan/environmental-impact-reports.shtml"
        )

    # --- Custom Footer Image ---
    footer_img = load_image(FOOTER_IMAGE)
    if footer_img:
        st.image(footer_img, use_container_width=True)
    else:
        st.caption("Footer image not found. Set FOOTER_IMAGE to a valid path or URL.")

# --- PAGE: BIRDS LIST ---
def render_birds():                   
    if st.button("Return to Home", key="return_home_birds"):
        st.session_state.page = "home"
        st.rerun()

    st.title("Cal Poly Pomona Bird Species")
    st.markdown(f"*{len(BIRD_SPECIES)} species documented on the wildlands of Cal Poly Pomona*")

    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        search_query = st.text_input(
            "Search for a bird by name",
            placeholder="e.g., 'hummingbird', 'hawk', 'California Quail'"
        )
    with col2:
        status_filter = st.selectbox(
            "Filter by Status",
            ["All", "Native", "Introduced", "Endangered/Threatened"]
        )
    with col3:
        st.write("")  # spacer
        st.write("")
        st.button("Add Bird", disabled=True, help="This feature is coming soon!")

    # Filter birds based on search
    filtered_birds = search_birds(search_query)

    # Apply status filter
    if status_filter != "All":
        def status_category(status):
            if status == "Native":
                return "Native"
            elif status == "Introduced":
                return "Introduced"
            else:
                return "Endangered/Threatened"
        filtered_birds = [b for b in filtered_birds if status_category(b["status"]) == status_filter]

    if not filtered_birds:
        st.warning("No birds found matching your filters. Try different criteria!")
    else:
        st.write(f"Showing {len(filtered_birds)} species")

        cols = st.columns(3)
        for idx, bird in enumerate(filtered_birds):
            with cols[idx % 3]:
                with st.container():
                    detail = get_bird_detail(bird["common"])
                    img_url = detail.get("image_url", DEFAULT_BIRD_IMAGE) if detail else DEFAULT_BIRD_IMAGE

                    if bird["status"] == "Native":
                        status_color = "green"
                        status_icon = "●"
                    elif bird["status"] == "Introduced":
                        status_color = "orange"
                        status_icon = "●"
                    else:
                        status_color = "red"
                        status_icon = "●"

                    st.markdown(f"""
                    <div style="border:1px solid #ddd; border-radius:10px; padding:15px; margin:10px 0; background-color:white; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                        <img src="{img_url}" style="width:100%; height:120px; object-fit:cover; border-radius:8px;">
                        <h4 style="margin:10px 0 5px 0; color:#2c3e50;">{bird['common']}</h4>
                        <p style="color:#2c3e50; font-size:0.9rem; margin:0;"><i>{bird['scientific']}</i></p>
                        <<p style="margin:5px 0; color: #000000;"><span style="color:{status_color};">{status_icon}</span> {bird['status']}</p>
                    </div>
                    """, unsafe_allow_html=True)

                    if st.button(f"View Details", key=f"view_{bird['common']}_{idx}"):
                        st.session_state.selected_bird = bird["common"]
                        st.session_state.page = "bird_detail"
                        st.rerun()

# --- PAGE: BIRD DETAIL ---
def render_bird_detail():
    bird_name = st.session_state.selected_bird
    if not bird_name:
        st.session_state.page = "birds"
        st.rerun()
        return

    bird_data = next((b for b in BIRD_SPECIES if b["common"] == bird_name), None)
    if not bird_data:
        st.error(f"Bird '{bird_name}' not found in the database.")
        if st.button("← Back to Birds"):
            st.session_state.page = "birds"
            st.rerun()
        return

    detail = get_bird_detail(bird_name)
    if not detail:
        detail = {
            "classification": "Data not available",
            "conservation_status": "Data not available",
            "image_url": DEFAULT_BIRD_IMAGE,
            "characteristics": "No additional information available for this species."
        }

    if st.button("← Back to Birds"):
        st.session_state.page = "birds"
        st.rerun()

    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(detail.get("image_url", DEFAULT_BIRD_IMAGE), use_container_width=True)
    with col2:
        st.title(bird_name)
        st.markdown(f"*{bird_data['scientific']}*")

        if bird_data["status"] == "Native":
            status_icon = "●"
            status_color = "green"
        elif bird_data["status"] == "Introduced":
            status_icon = "●"
            status_color = "orange"
        else:
            status_icon = "●"
            status_color = "red"
        st.markdown(f"**Status:** <span style='color:{status_color};'>{status_icon}</span> {bird_data['status']}", unsafe_allow_html=True)
        st.markdown(f"**Conservation Status:** {detail.get('conservation_status', 'Data not available')}")
        st.markdown(f"**Scientific Classification:** {detail.get('classification', 'Data not available')}")

    st.subheader("Overview")
    st.write(detail.get("characteristics", "No description available."))


    st.markdown("---")
    st.subheader("Search this species online")
    col1, col2 = st.columns(2)
    with col1:
        inat_url = f"https://www.inaturalist.org/?utm_source=google_cpc&utm_medium=ad_grant&utm_campaign=cbc_ggrant_Brand_Esp_Max_Clicks&gad_source=1&gad_campaignid=23370780638&gbraid=0AAAABAxkD6uBUJorIGtkSm0siNVqePmNF"
        st.link_button("View on iNaturalist", inat_url)
    with col2:
        cnddb_url = "https://wildlife.ca.gov/Data/CNDDB/Plants-and-Animals"
        st.link_button("Search CNDDB (RareFind)", cnddb_url)

# --- MAIN ROUTING ---
def main():
    if st.session_state.page == "home":
        render_home()
    elif st.session_state.page == "birds":
        render_birds()
    elif st.session_state.page == "bird_detail":
        render_bird_detail()
    else:
        render_home()

if __name__ == "__main__":
    main()