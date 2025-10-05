#!/usr/bin/env python3
"""
Test script to verify MandiBot API functionality
"""

import requests
import json
from datetime import datetime, timedelta

def test_mandi_api():
    """Test the data.gov.in mandi API"""
    print("🌾 Testing MandiBot API Connection...")
    
    base_url = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"
    api_key = "579b464db66ec23bdd000001821e64e87e204b907bc5b548880a106d"
    
    # Get today's and yesterday's dates
    today = datetime.now().strftime("%d/%m/%Y")
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%d/%m/%Y")
    print(f"📅 Testing for today: {today}")
    print(f"📅 Testing for yesterday: {yesterday}")
    
    # Test parameters for today
    params_today = {
        "api-key": api_key,
        "format": "json",
        "limit": "5",
        "filters[commodity]": "Tomato",
        "filters[arrival_date]": today
    }
    
    # Test parameters for yesterday
    params_yesterday = {
        "api-key": api_key,
        "format": "json",
        "limit": "5",
        "filters[commodity]": "Tomato",
        "filters[arrival_date]": yesterday
    }
    
    try:
        print("🔄 Testing Today's Data...")
        response_today = requests.get(base_url, params=params_today, timeout=10)
        response_today.raise_for_status()
        data_today = response_today.json()
        
        print(f"✅ Today's API Status: {data_today.get('status', 'Unknown')}")
        print(f"📊 Today's Records: {data_today.get('count', 0)}")
        
        print("\n🔄 Testing Yesterday's Data...")
        response_yesterday = requests.get(base_url, params=params_yesterday, timeout=10)
        response_yesterday.raise_for_status()
        data_yesterday = response_yesterday.json()
        
        print(f"✅ Yesterday's API Status: {data_yesterday.get('status', 'Unknown')}")
        print(f"📊 Yesterday's Records: {data_yesterday.get('count', 0)}")
        
        # Show sample records
        if data_today.get('records'):
            print(f"\n🎯 Today's Sample Record:")
            record = data_today['records'][0]
            print(f"   State: {record.get('state', 'N/A')}")
            print(f"   Market: {record.get('market', 'N/A')}")
            print(f"   Modal Price: ₹{record.get('modal_price', 'N/A')}/quintal")
            print(f"   Date: {record.get('arrival_date', 'N/A')}")
        else:
            print("⚠️  No records found for today")
            
        if data_yesterday.get('records'):
            print(f"\n🎯 Yesterday's Sample Record:")
            record = data_yesterday['records'][0]
            print(f"   State: {record.get('state', 'N/A')}")
            print(f"   Market: {record.get('market', 'N/A')}")
            print(f"   Modal Price: ₹{record.get('modal_price', 'N/A')}/quintal")
            print(f"   Date: {record.get('arrival_date', 'N/A')}")
        else:
            print("⚠️  No records found for yesterday")
            
        print("\n✅ API Test Completed Successfully!")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"❌ API Request Error: {str(e)}")
        return False
    except json.JSONDecodeError:
        print("❌ JSON Parsing Error")
        return False
    except Exception as e:
        print(f"❌ Unexpected Error: {str(e)}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("🌾 MandiBot API Test")
    print("=" * 50)
    
    success = test_mandi_api()
    
    print("\n" + "=" * 50)
    if success:
        print("🎉 All tests passed! MandiBot is ready to use.")
        print("\nTo run the application:")
        print("   streamlit run app.py")
    else:
        print("⚠️  Some tests failed. Check your internet connection.")
    print("=" * 50)
