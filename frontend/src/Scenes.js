import React from 'react';
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';
import Box from '@mui/material/Box';
import { buttonStyle } from './styles';

function Scenes() {
  const triggerScene = (url) => {
    fetch(`http://localhost:5000${url}`)
      .then(response => response.text())
      .then(data => alert(data))
      .catch(error => console.error('Error:', error));
  };

  return (
    <Box 
      display="flex" 
      justifyContent="center" 
      alignItems="center" 
      height="calc(100vh - 60px)" // Adjust height to account for the title area
      padding="0"
      margin="0"
      style={{
        background: 'linear-gradient(to bottom, #1D4E89, #87CEEB)', // Same gradient background
        width: '100%',
        overflow: 'hidden',
      }}
    >
      <Stack 
        spacing={4}
        alignItems="center" // Center stack items horizontally
      >
        <Button
          variant="contained"
          style={{ ...buttonStyle, backgroundColor: '#FFB74D' }} // Soft warm orange
          onClick={() => triggerScene('/wind_down')}
          onMouseEnter={(e) => e.currentTarget.style.transform = 'scale(1.05)'}
          onMouseLeave={(e) => e.currentTarget.style.transform = 'scale(1)'}
        >
          Wind down scene
        </Button>
        <Button
          variant="contained"
          style={{ ...buttonStyle, backgroundColor: '#64B5F6' }} // Soft calm blue
          onClick={() => triggerScene('/work_from_home')}
          onMouseEnter={(e) => e.currentTarget.style.transform = 'scale(1.05)'}
          onMouseLeave={(e) => e.currentTarget.style.transform = 'scale(1)'}
        >
          Work from home scene
        </Button>
      </Stack>
    </Box>
  );
}

export default Scenes;
