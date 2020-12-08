function iniciarMap() {
    var coord = { lat: -33.4999176, lng: -70.6164671 };
    var map = new google.map.Map(document.getElementById('map'), {
        zoom: 10,
        center: coord
    });
}