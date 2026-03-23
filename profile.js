// profile.js

// Mock MicrosoftID for testing
const microsoftID = "test-user-001";

// Mock load function
function loadProfile() {
  const data = {
    FirstName: "Chad",
    LastName: "MacDonald",
    BusinessName: "My Farm",
    Email: "chad@example.com",
    Phone: "123-456-7890",
    Address1: "123 Main St",
    Address2: "Unit 5",
    City: "Sydney",
    State: "NS",
    PostalCode: "B1P 6M9"
  };

  document.getElementById('firstName').value = data.FirstName;
  document.getElementById('lastName').value = data.LastName;
  document.getElementById('businessName').value = data.BusinessName;
  document.getElementById('email').value = data.Email;
  document.getElementById('phone').value = data.Phone;
  document.getElementById('address1').value = data.Address1;
  document.getElementById('address2').value = data.Address2;
  document.getElementById('city').value = data.City;
  document.getElementById('state').value = data.State;
  document.getElementById('postalCode').value = data.PostalCode;
}

loadProfile();

// Mock form submission
document.getElementById('profileForm').addEventListener('submit', function(e) {
  e.preventDefault();

  const profileData = {
    MicrosoftID: microsoftID,
    FirstName: document.getElementById('firstName').value,
    LastName: document.getElementById('lastName').value,
    BusinessName: document.getElementById('businessName').value,
    Email: document.getElementById('email').value,
    Phone: document.getElementById('phone').value,
    Address1: document.getElementById('address1').value,
    Address2: document.getElementById('address2').value,
    City: document.getElementById('city').value,
    State: document.getElementById('state').value,
    PostalCode: document.getElementById('postalCode').value
  };

  console.log("Saved profile (mock):", profileData);
  alert("Profile saved! Check console for mock data.");
});