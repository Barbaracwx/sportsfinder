// Get form elements and userInfo section
const submitButton = document.getElementById('submitButton');
const userAge = document.getElementById('userAge');
const userGender = document.getElementById('userGender');
const userSports = document.getElementById('userSports');
const userLocation = document.getElementById('userLocation');
const userInfo = document.getElementById('userInfo');
const profileForm = document.querySelector('.profile-form');

// Event listener for form submission
submitButton.addEventListener('click', function () {
    // Get selected age
    const age = document.querySelector('input[name="age"]:checked');
    const ageValue = age ? age.value : 'Not specified';

    // Get selected gender
    const gender = document.querySelector('input[name="gender"]:checked');
    const genderValue = gender ? gender.value : 'Not specified';

    // Get selected sports and their skill levels
    const sports = [];
    const skillLevels = [];
    document.querySelectorAll('input[name="sports"]:checked').forEach((checkbox) => {
        const sport = checkbox.value;
        sports.push(sport);

        // Get the skill level for the selected sport
        const skillSelect = document.getElementById(`${sport.replace(/\s/g, '').toLowerCase()}-skill`);
        if (skillSelect && skillSelect.style.display !== 'none') {
            const skillValue = skillSelect.value;
            skillLevels.push(`${sport}: ${skillValue}`);
        }
    });
    const sportsValue = sports.length > 0 ? sports.join(', ') : 'None';
    const skillLevelsValue = skillLevels.length > 0 ? skillLevels.join(', ') : 'None';

    // Get selected location
    const location = document.querySelector('input[name="location"]:checked');
    const locationValue = location ? location.value : 'Not specified';

    // Display user profile
    userAge.textContent = `Age: ${ageValue}`;
    userGender.textContent = `Gender: ${genderValue}`;
    userSports.textContent = `Sports: ${sportsValue} | Skill Levels: ${skillLevelsValue}`;
    userLocation.textContent = `Location: ${locationValue}`;

    // Show the profile section and hide the form
    userInfo.style.display = 'block';
    profileForm.style.display = 'none';
});

// Show skill level dropdown when a sport is selected
document.querySelectorAll('input[name="sports"]').forEach((checkbox) => {
    checkbox.addEventListener('change', function () {
        const sport = this.value.replace(/\s/g, '').toLowerCase(); // Handle spaces in sport names
        const skillSelect = document.getElementById(`${sport}-skill`);
        skillSelect.style.display = this.checked ? 'block' : 'none';
    });
});
