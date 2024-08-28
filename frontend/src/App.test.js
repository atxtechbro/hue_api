import { render, screen, fireEvent } from '@testing-library/react';
import Scenes from './Scenes';

test('renders Scenes component with scene buttons', () => {
  render(<Scenes />);
  const windDownButton = screen.getByText(/Wind down scene/i);
  expect(windDownButton).toBeInTheDocument();
  const workFromHomeButton = screen.getByText(/Work from home scene/i);
  expect(workFromHomeButton).toBeInTheDocument();
});

test('renders CircadianSettings component', () => {
  render(<Scenes />);
  const startTimeInput = screen.getByLabelText(/Start Time/i);
  expect(startTimeInput).toBeInTheDocument();
  fireEvent.change(startTimeInput, { target: { value: '07:00' } });
  expect(startTimeInput.value).toBe('07:00');

  const submitButton = screen.getByText(/Save/i);
  fireEvent.click(submitButton);
  
  // Check for feedback after form submission
  const feedbackMessage = screen.getByText(/Circadian lighting settings updated successfully./i);
  expect(feedbackMessage).toBeInTheDocument();
});
