fetch('https://ipinfo.io/json')
  .then(response => response.json())
  .then(data => {
    console.log(`IP 地址: ${data.ip}`);
    console.log(`国家: ${data.country}`);
    console.log(`地区: ${data.region}`);
    console.log(`城市: ${data.city}`);
  })
  .catch(error => console.error('Error fetching location data:', error));

