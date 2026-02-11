import { render, screen } from '@testing-library/react';
import Home from '../frontend/src/pages/Home';

test('renders home page title', () => {
  render(<Home />);
  const linkElement = screen.getByText(/Welcome to Apex Digital AI/i);
  expect(linkElement).toBeInTheDocument();
});
