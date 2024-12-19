// Simulated Disaster Alerts for India
const disasterAlerts = [
    { type: 'Flood', location: 'Assam', status: 'Ongoing', time: '12:30 PM' },
    { type: 'Cyclone', location: 'Odisha', status: 'Upcoming', time: '3:00 PM' },
    { type: 'Earthquake', location: 'Delhi NCR', status: 'Ongoing', time: '11:45 AM' },
  ];

// Function to populate the marquee
const displayAlerts = () => {
  const alertsContainer = document.querySelector('.marquee-content');
  if (!alertsContainer) return;

  if (disasterAlerts.length === 0) {
    alertsContainer.innerHTML = 'No alerts at the moment. Stay safe!';
    return;
  }

  // Combine all alerts into a single string with line breaks
  alertsContainer.innerHTML = disasterAlerts
    .map(
      (alert) =>
        `<p><strong>${alert.type}</strong> in <strong>${alert.location}</strong> - <em>${alert.status}</em> at <strong>${alert.time}</strong>.</p>`
    )
    .join('');
};

// Initialize the marquee
displayAlerts();

// Function to show/hide the "Other" disaster type input field
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
