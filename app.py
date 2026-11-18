import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from pathlib import Path

# -------------------------------------------------
# Page configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Data Explorer & COVID-19 Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Data Explorer & COVID-19 Dashboard")
st.caption("Explore datasets, view summary statistics, and visualize COVID-19 case trends.")

# -------------------------------------------------
# Helper functions
# -------------------------------------------------
@st.cache_data
def load_csv(file_path):
    return pd.read_csv(file_path)


def show_data_explorer():
    st.header("🔎 Data Explorer")
    st.write("Upload a CSV or Excel file to explore its contents.")

    uploaded_file = st.file_uploader(
        "Choose a dataset",
        type=["csv", "xlsx"],
        key="general_dataset"
    )

    if uploaded_file is None:
        st.info("Upload a CSV or Excel file to begin exploring your data.")
        return

    try:
        if uploaded_file.name.lower().endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        if df.empty:
            st.warning("The uploaded file has no rows.")
            return

        st.subheader("Dataset Preview")
        st.dataframe(df.head(10), use_container_width=True)

        row_count, column_count = df.shape
        col1, col2, col3 = st.columns(3)
        col1.metric("Total rows", f"{row_count:,}")
        col2.metric("Total columns", f"{column_count:,}")
        col3.metric("Missing values", f"{int(df.isna().sum().sum()):,}")

        with st.expander("Column names and data types"):
            info_df = pd.DataFrame({
                "Column": df.columns.astype(str),
                "Data type": df.dtypes.astype(str).values,
                "Missing values": df.isna().sum().values
            })
            st.dataframe(info_df, use_container_width=True)

        st.subheader("Summary Statistics")
        st.dataframe(df.describe(include="all").transpose(), use_container_width=True)

        st.subheader("Filter the Dataset")
        filter_column = st.selectbox(
            "Choose a column",
            options=df.columns.tolist(),
            key="filter_column"
        )

        values = df[filter_column].dropna().unique().tolist()
        if values:
            selected_value = st.selectbox(
                "Choose a value",
                options=values,
                key="filter_value"
            )
            filtered_df = df[df[filter_column] == selected_value]
            st.write(f"Rows matching **{selected_value}**: {len(filtered_df)}")
            st.dataframe(filtered_df, use_container_width=True)
        else:
            st.info("This column contains no non-empty values to filter.")

        numeric_columns = df.select_dtypes(include="number").columns.tolist()
        if numeric_columns:
            st.subheader("Numeric Column Visualization")
            chart_column = st.selectbox(
                "Choose a numeric column",
                options=numeric_columns,
                key="numeric_chart_column"
            )
            fig = px.histogram(
                df,
                x=chart_column,
                title=f"Distribution of {chart_column}"
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No numeric columns are available for a histogram.")

        # Optional MBA-specific metrics, shown only when the column exists.
        if "gmat" in df.columns:
            st.subheader("GMAT Statistics")
            gmat = pd.to_numeric(df["gmat"], errors="coerce").dropna()
            if not gmat.empty:
                c1, c2, c3 = st.columns(3)
                c1.metric("Average GMAT score", f"{gmat.mean():.2f}")
                c2.metric("Highest GMAT score", f"{gmat.max():.0f}")
                c3.metric("Total GMAT scores", f"{len(gmat):,}")

    except Exception as error:
        st.error(f"Unable to read this file: {error}")
        st.info("Check that the file is a valid CSV or Excel file and that its columns are formatted correctly.")


def show_covid_dashboard():
    st.header("🦠 COVID-19 Dashboard")
    st.write("View sample COVID-19 case trends by date and state.")

    # The downloaded sample file is named covid-data.csv.
    default_file = Path(__file__).parent / "covid-data.csv"
    uploaded_covid_file = st.file_uploader(
        "Or upload a COVID-19 CSV file",
        type=["csv"],
        key="covid_dataset"
    )

    try:
        if uploaded_covid_file is not None:
            covid_df = pd.read_csv(uploaded_covid_file)
        elif default_file.exists():
            covid_df = load_csv(str(default_file))
        else:
            st.warning("Place `covid-data.csv` in the same folder as `app.py`, or upload a COVID-19 CSV file above.")
            return

        required_columns = {"Date", "Cases", "State"}
        missing_columns = required_columns - set(covid_df.columns)
        if missing_columns:
            st.error(
                "The COVID-19 dataset must contain these columns: Date, Cases, State. "
                f"Missing: {', '.join(sorted(missing_columns))}"
            )
            st.write("Columns found:", covid_df.columns.tolist())
            return

        covid_df["Date"] = pd.to_datetime(covid_df["Date"], errors="coerce")
        covid_df["Cases"] = pd.to_numeric(covid_df["Cases"], errors="coerce")
        covid_df = covid_df.dropna(subset=["Date", "Cases", "State"])

        if covid_df.empty:
            st.warning("There are no valid records to display.")
            return

        states = sorted(covid_df["State"].astype(str).unique().tolist())
        selected_state = st.selectbox("Select a state", ["All States"] + states)

        if selected_state == "All States":
            filtered_df = covid_df
        else:
            filtered_df = covid_df[covid_df["State"].astype(str) == selected_state]

        total_cases = int(filtered_df["Cases"].sum())
        average_cases = filtered_df["Cases"].mean()
        highest_cases = int(filtered_df["Cases"].max())

        metric1, metric2, metric3 = st.columns(3)
        metric1.metric("Total reported cases", f"{total_cases:,}")
        metric2.metric("Average cases per record", f"{average_cases:,.1f}")
        metric3.metric("Highest cases in a record", f"{highest_cases:,}")

        fig = px.line(
            filtered_df.sort_values("Date"),
            x="Date",
            y="Cases",
            color="State" if selected_state == "All States" else None,
            markers=True,
            title="COVID-19 Cases Over Time"
        )
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("COVID-19 Records")
        st.dataframe(
            filtered_df.sort_values("Date"),
            use_container_width=True
        )

        st.download_button(
            "Download filtered data",
            data=filtered_df.to_csv(index=False).encode("utf-8"),
            file_name="filtered-covid-data.csv",
            mime="text/csv"
        )

        st.caption("Note: The provided covid-data.csv is sample learning data, not official historical statistics.")

    except Exception as error:
        st.error(f"Unable to load the COVID-19 dataset: {error}")


# -------------------------------------------------
# App navigation
# -------------------------------------------------
data_tab, covid_tab, about_tab = st.tabs(
    ["Data Explorer", "COVID-19 Dashboard", "About"]
)

with data_tab:
    show_data_explorer()

with covid_tab:
    show_covid_dashboard()

with about_tab:
    st.header("About this project")
    st.write(
        "This beginner-friendly Streamlit project demonstrates file uploads, "
        "Pandas data analysis, interactive filters, metrics, Plotly charts, "
        "and CSV downloads."
    )
    st.write("Built with Python, Streamlit, Pandas, Matplotlib, and Plotly.")
