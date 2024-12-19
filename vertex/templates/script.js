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

// Header hide on scroll
let lastScrollTop = 0;
const header = document.querySelector("header");

window.addEventListener("scroll", () => {
  const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

  if (scrollTop > lastScrollTop) {
    // Scrolling down
    header.style.top = `-${header.offsetHeight}px`; // Hides the header completely
  } else {
    // Scrolling up
    header.style.top = "0"; // Shows the header
  }

  lastScrollTop = scrollTop;
});

// Mobile menu toggle
const menuToggle = document.querySelector('.menu-toggle');
const menu = document.querySelector('.menu');

menuToggle.addEventListener('click', () => {
  menu.classList.toggle('active'); // Toggle menu visibility
});


// Ensure that the volunteer link opens the registration form in a new tab
document.getElementById('volunteer-link').addEventListener('click', function(e) {
  e.preventDefault(); // Prevent default link behavior
  window.open('volunteer-registration.html', '_blank'); // Open the volunteer registration page in a new tab
});


// Handle the form submission
document.getElementById('volunteer-form').addEventListener('submit', function(event) {
  event.preventDefault();

  // Simple form validation
  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  const phone = document.getElementById('phone').value;
  const location = document.getElementById('location').value;
  const skills = document.getElementById('skills').value;
  const availability = document.getElementById('availability').value;

  if (!name || !email || !phone || !location || !skills || !availability) {
    alert('Please fill in all fields');
    return;
  }

  // Show a success message or submit the form
  alert('Thank you for registering as a volunteer!');
  document.getElementById('volunteer-form').reset(); // Clear the form
});
