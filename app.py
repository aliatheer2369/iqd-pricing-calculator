import streamlit as st

# إعدادات وتنسيق الصفحة
st.set_page_config(page_title="حاسبة تسعير المنتجات", page_icon="💰")
st.title("💰 حاسبة تسعير المنتجات والأرباح")
st.write("أداة تفاعلية لحساب تكلفة الشراء بالدينار العراقي وسعر البيع المقترح بناءً على نسبة الربح.")

# مدخلات البيانات
product_name = st.text_input("اسم المنتج", value="Vape")
price_usd = st.number_input("سعر الشراء بالدولار ($)", min_value=0.0, value=9.0, step=0.5)
exchange_rate = st.number_input("سعر صرف $100 بالدينار العراقي", value=150000, step=500)
profit_percent = st.slider("نسبة الربح المطلوبة (%)", min_value=5, max_value=100, value=20)

# الحسابات الرياضية
price_iqd = price_usd * (exchange_rate / 100)
final_price = price_iqd * (1 + (profit_percent / 100))

# عرض النتائج في بطاقات مرتبة
st.divider()
st.subheader(f"📊 نتائج التسعير لـ: {product_name}")

col1, col2 = st.columns(2)
with col1:
    st.metric("التكلفة بالدينار العراقي", f"{price_iqd:,.0f} د.ع")
with col2:
    st.metric("سعر البيع المقترح", f"{final_price:,.0f} د.ع")