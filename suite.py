from air_canada_test import AirCanadaTest

testCase = AirCanadaTest

# Navigate to Site
testCase.openHomeScreen("https://www.aircanada.com/")

# Validate Site Homepage Title
testCase.validateTitle("Book Flights Online | Air Canada")

# Navigate to Flight Status Page
testCase.navigateToFlightStatus("Air Canada Flight Status | Real-Time Updates")

# Close Main Navigation
testCase.closeMainNavigation()

# Find a Flight
testCase.findAFlight("1234")

testCase.tearDown()