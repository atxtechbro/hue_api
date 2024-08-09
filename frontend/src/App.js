import React from 'react';
import Scenes from './Scenes';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import { containerStyle, titleTextStyle } from './styles';

function App() {
  return (
    <Container maxWidth="false" disableGutters={true} style={containerStyle}>
      <Box 
        sx={{
          padding: '20px 10px', 
          textAlign: 'center', 
          position: 'relative', 
          zIndex: 1,
          background: 'linear-gradient(to bottom, #1D4E89, #87CEEB)', // Extend the gradient to cover the title area
          color: '#FFFFFF', // White text color for contrast
        }}
      >
        <Typography 
          variant="h3" 
          component="h1" 
          gutterBottom
          style={{
            ...titleTextStyle,
            textShadow: '1px 1px 3px rgba(0, 0, 0, 0.7)', // Subtle text shadow for depth
            marginBottom: '20px', // Add spacing below the title
          }}
        >
          Hue Lighting Demo
        </Typography>
      </Box>
      <Scenes />
    </Container>
  );
}

export default App;
