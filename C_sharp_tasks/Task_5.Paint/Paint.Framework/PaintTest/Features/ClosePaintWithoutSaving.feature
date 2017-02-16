Feature: Close Paint without saving

Scenario: Change picture and close app without saving
	Given Main Paint window opened
	When I open 'Address' folder, select picture 'Picture' 
		And I click Select menu item
		And I click Select all button
		And I click 'Cut'
		And I click 'Close' application
		And I click 'Do not save' 
	Then Paint is closed
