// 1. نصنعو الخريطة ونوجهوها لتونس 
const map = L.map('map').setView([33.8869, 9.5375], 6);

// 2. نزيدو طبقة الخريطة الداكنة المجانية 
L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}', {
    attribution: 'Tiles &copy; Esri &mdash; Esri, DeLorme, NAVTEQ',
    maxZoom: 16
}).addTo(map);

// 3. نجيبو الداتا من سيرفر Flask
fetch('/api/sites')
    .then(response => response.json())
    .then(sites => {
        sites.forEach(site => {
            let marker = L.marker([site.latitude, site.longitude]).addTo(map);
            
            // التغيير هوني: زدنا التصويرة في الـ Popup وكبرنا العرض شوية (220px)
            marker.bindPopup(`
                <div style="text-align: left; width: 220px;">
                    <img src="${site.image_url}" width="200">
                    <h3 style="margin-bottom: 5px; color: #d32f2f; margin-top: 0;">${site.name}</h3>
                    <p style="margin-top: 0; font-size: 13px;"><b>Category:</b> ${site.category}</p>
                    <p style="font-size: 14px;">${site.description}</p>
                </div>
            `);
        });
    })
    .catch(error => {
        console.error('فما مشكلة في جلب البيانات:', error);
    });