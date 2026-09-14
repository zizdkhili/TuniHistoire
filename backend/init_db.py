import sqlite3

# 1. الاتصال بقاعدة البيانات
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# 2. إنشاء الجدول
cursor.execute('''
CREATE TABLE IF NOT EXISTS sites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    category TEXT,
    image_url TEXT,
    latitude REAL,
    longitude REAL
)
''')

# 3. مسح البيانات القديمة
cursor.execute('DELETE FROM sites')

# 4. قائمة المواقع بتصاور Unsplash (بدون بلوكاج)
sites_data = [
    ("Ribat de Monastir", "Built in 796 AD, it is the oldest and best-preserved ribat in the Maghreb.", "Medieval / Ribats", "https://images.unsplash.com/photo-1539617546058-a8689ff8a381?w=400", 35.7643, 10.8286),
    ("Ribat de Sousse", "A 9th-century coastal fortress, part of the same defensive chain as Monastir.", "Medieval / Ribats", "https://images.unsplash.com/photo-1583262624536-12a91e5e6e61?w=400", 35.8256, 10.6412),
    ("Mareth Line Military Museum", "Museum about the WWII Mareth Line, a 45km defensive line.", "World War II", "https://images.unsplash.com/photo-1596704179377-6218151edb75?w=400", 33.6333, 10.3000),
    ("Kasserine Pass", "Site of a major WWII battle in February 1943 between US forces and the German Afrika Korps.", "World War II", "https://images.unsplash.com/photo-1582236111306-39ce3d5483a9?w=400", 35.1667, 8.7833),
    ("Ras El Blat Marine Museum", "Naval history museum opened in 2022, covering Tunisian maritime history.", "Antiquity / Modern", "https://images.unsplash.com/photo-1518342415174-8452be42d075?w=400", 37.2744, 9.8739),
    ("Carthage Archaeological Site", "Punic Wars era military and naval history, Byrsa hill, and Punic ports.", "Antiquity", "https://images.unsplash.com/photo-1627931326402-53b7501a3501?w=400", 36.8528, 10.3233),
    ("Amphitheatre of El Jem", "One of the most accomplished examples of Roman architecture...", "Antiquity", "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/El_Jem_Amphitheatre_2012.jpg/400px-El_Jem_Amphitheatre_2012.jpg", 35.2964, 10.7069)

# 5. إدخال كل المواقع
for site in sites_data:
    cursor.execute('''
    INSERT INTO sites (name, description, category, image_url, latitude, longitude)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', site)

# 6. حفظ وإغلاق
conn.commit()
conn.close()
print("✅ Database updated with Unsplash images!")