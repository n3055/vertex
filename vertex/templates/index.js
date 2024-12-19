// Simulated Disaster Alerts for India
const disasterAlerts = [
    { type: 'Flood', location: 'Assam', status: 'Ongoing', time: '12:30 PM' },
    { type: 'Cyclone', location: 'Odisha', status: 'Upcoming', time: '3:00 PM' },
    { type: 'Earthquake', location: 'Delhi NCR', status: 'Ongoing', time: '11:45 AM' },
    { type: 'Landslide', location: 'Himachal Pradesh', status: 'Ongoing', time: '10:15 AM' },
    { type: 'Forest Fire', location: 'Uttarakhand', status: 'Upcoming', time: '4:00 PM' },
    { type: 'Heat Wave', location: 'Rajasthan', status: 'Ongoing', time: '1:00 PM' },
    { type: 'Heavy Rainfall', location: 'Mumbai', status: 'Ongoing', time: '12:00 PM' },
    { type: 'Tsunami', location: 'Chennai', status: 'Upcoming', time: '5:30 PM' }
  ];
  
  // Function to display alerts in a marquee
  const displayAlerts = () => {
    const alertsContainer = document.getElementById('real-time-alerts');
    alertsContainer.innerHTML = ''; // Clear existing content
  
    if (disasterAlerts.length === 0) {
      alertsContainer.innerHTML = '<p>No alerts at the moment. Stay safe!</p>';
      return;
    }
  
    const marqueeElement = document.createElement('div');
    marqueeElement.className = 'marquee';
  
    disasterAlerts.forEach((alert) => {
      const alertElement = document.createElement('p');
      alertElement.innerHTML = `
        <strong>${alert.type}</strong> in <strong>${alert.location}</strong> - 
        <em>${alert.status}</em> at <strong>${alert.time}</strong>.
      `;
      marqueeElement.appendChild(alertElement);
    });
  
    alertsContainer.appendChild(marqueeElement);
  };
  
  // Initialize the display
  displayAlerts();
  
  
  function toggleOtherField() {
    const disasterType = document.getElementById('disaster-type').value;
    const otherDisasterField = document.getElementById('other-disaster-container');
    
    // If the "Other" option is selected, show the input field; otherwise, hide it
    if (disasterType === 'other') {
      otherDisasterField.style.display = 'block';
    } else {
      otherDisasterField.style.display = 'none';
    }
  }