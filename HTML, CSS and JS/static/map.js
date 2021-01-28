function chooseColor(type) {
    switch (type) {
    case "large":
      return "yellow";
    case "micro":
      return "red";
    case "regional":
      return "orange";
    case "brewpub":
      return "green";
    case "contract":
      return "purple";
    default:
      return "black";
    }
  }
  
 var mb =[]
 var large =[]
 var sta = []
 url="/map_data";




d3.json(url, function(response){

  resp = response
  size = Object.values(resp).length
    


  fmb=Object.values(resp).filter(user => user.brewery_type === "micro");
  st =Object.values(resp).filter(user => user.state === "New York");
  console.log(fmb.length)

    
  for (var i = 0; i < size; i++) {

      // fmb=Object.values(resp).filter(user => user.brewery_type === "micro");
      var lat = resp[i].latitude;
      var long = resp[i].longitude;
       
       
      // if (resp.brewery_type=="micro"){
                     
      // //  for (var m=0; m<fmb.length; m++){
      // //       // fmb=Object.values(resp).filter(user => user.brewery_type === "micro");
      //       var lat1 = resp[i].latitude;
      //       var long1 = resp[i].longitude;
       
      // mb.push(
      // L.circle([lat1, long1],
      //     {
      //       fillOpacity: 1,
      //       // color: "blue",
      //       fillColor:chooseColor(fmb[i].brewery_type),
      //       radius:10000
      //     }).bindPopup("<h3> Type of Brewery: " + fmb[i].brewery_type+"<h3> Name: " + fmb[i].name +
      //        "<h3>City: " + fmb[i].city + "<h3>Url :" + fmb[i].website_url

      //     ));

      // }

      // else {

       large.push(

        L.circle([lat, long],
          {
            fillOpacity: 1,
            // color: "blue",
            fillColor:chooseColor(resp[i].brewery_type),
            radius:10000
          }).bindPopup("<h3> Type of Brewery: " + resp[i].brewery_type+"<h3> Name: " + resp[i].name +
                  "<h3>City: " + resp[i].city + "<h3>Url :" +resp[i].website_url )

       );
        };

   for (var m = 0;  m < fmb.length; m++) {

      var lat1 = fmb[m].latitude;
      var long1 = fmb[m].longitude;
       
      mb.push(
      L.circle([lat1, long1],
          {
            fillOpacity: 1,
            // color: "blue",
            fillColor:chooseColor(fmb[m].brewery_type),
            radius:10000
          }).bindPopup("<h3> Type of Brewery: " + fmb[m].brewery_type+"<h3> Name: " + fmb[m].name +
             "<h3>City: " + fmb[m].city + "<h3>Url :" +fmb[m].website_url 
          ));
    

    };

   for (var n = 0;  n < st.length; n++) {

      var lat2 = st[n].latitude;
      var long2 = st[n].longitude;
       
      sta.push(
      L.circle([lat2, long2],
          {
            fillOpacity: 1,
            // color: "blue",
            fillColor: chooseColor(st[n].brewery_type),
            radius:10000
          }).bindPopup("<h3> Type of Brewery: " + st[n].brewery_type+"<h3> Name: " + st[n].name +
             "<h3>City: " + st[n].city + "<h3>Url :" +st[n].website_url 
          ));
    

    };

    
    
      
     

                   
  

  var streetmap=L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
  tileSize: 512,
  maxZoom: 18,
  zoomOffset: -1,
  id: "mapbox/streets-v11",
  accessToken: API_KEY
    })

    var micro = L.layerGroup(mb);
    var lg = L.layerGroup(large);
    var sta1 = L.layerGroup(sta);

    var baseMaps = {
      "Street Map": streetmap,
      
    };

    var overlayMaps = {
      "Microbreweries": micro,
      "All": lg,
      "New York": sta1
    };

    var myMap = L.map("map", {
      center: [32.17, -82.90],
      zoom: 5,
      layers: [streetmap,lg, micro,sta1]
    });

    L.control.layers ( baseMaps, overlayMaps, {
      collapsed: false
    }).addTo(myMap);




    var legend = L.control({ position: 'bottomright' });
      legend.onAdd = function (myMap) {
        var div = L.DomUtil.create('div', 'info legend'),
          grades = ["large","micro","regional","contract", "brewpub"]
          
        // loop through density intervals and generate a label with a colored square for each interval
        for (var i = 0; i < grades.length; i++) {
          div.innerHTML +=
                  '<i style="background:' + chooseColor(grades[i]) + '"></i> ' +
                  grades[i] + (grades[i] ? '&ndash;' + grades[i] + '<br>' : '+'); 
        }
        return div;
      };
    legend.addTo(myMap);
        

  });  
  



       
