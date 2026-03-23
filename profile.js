// profile.js

// Load profile from backend API and prefill form
async function loadProfile() {
  try {
    const res = await fetch('http://127.0.0.1:5000/api/profile'); // Flask API URL
    if (!res.ok) throw new Error("Profile not found");

    const data = await res.json();

    document.getElementById('firstName').value = data.FirstName || '';
    document.getElementById('lastName').value = data.LastName || '';
    document.getElementById('businessName').value = data.BusinessName || '';
    document.getElementById('email').value = data.Email || '';
    document.getElementById('phone').value = data.Phone || '';
    document.getElementById('address1').value = data.Address1 || '';
    document.getElementById('address2').value = data.Address2 || '';
    document.getElementById('city').value = data.City || '';
    document.getElementById('state').value = data.State || '';
    document.getElementById('postalCode').value = data.PostalCode || '';

  } catch (err) {
    console.error("Error loading profile:", err);
  }
}

// Handle form submission to backend API
document.getElementById('profileForm').addEventListener('submit', async function(e) {
  e.preventDefault();

  const profileData = {
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

  try {
    const res = await fetch('http://127.0.0.1:5000/api/profile', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(profileData)
    });

    const result = await res.json();

    if (res.ok) {
      alert("✅ Profile saved successfully!");
      loadProfile(); // Refresh form
    } else {
      alert("❌ Error saving profile: " + (result.error || "Unknown error"));
    }

  } catch (err) {
    console.error("Error saving profile:", err);
    alert("❌ Error saving profile. Check console.");
  }
});

// Load profile when page loads
loadProfile();