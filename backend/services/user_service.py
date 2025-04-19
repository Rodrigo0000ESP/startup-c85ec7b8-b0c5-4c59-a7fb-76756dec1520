from backend.utils import ai_analysis

def get_ai_insights():
    aggregated_data = data_aggregation_utilities.get_data()
    insights = ai_analysis.analyze_data(aggregated_data)
    return insights