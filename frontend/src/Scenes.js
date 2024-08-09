import React from 'react';
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';
import Box from '@mui/material/Box';

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
      height="100vh"
      padding="20px"
      style={{
        background: 'linear-gradient(to bottom, #1D4E89, #87CEEB)'
      }}
    >
      <Stack 
        spacing={4}
      >
        <Button
          variant="contained"
          style={{ 
            backgroundColor: '#FFB74D', 
            color: 'white', 
            fontSize: '18px', 
            letterSpacing: '0.75px', 
            fontWeight: 'bold',
            textTransform: 'none',
            borderRadius: '8px',
            boxShadow: '0px 4px 6px rgba(0, 0, 0, 0.1)',
            transition: 'transform 0.2s ease-in-out',
          }}
          onClick={() => triggerScene('/wind_down')}
          onMouseEnter={(e) => e.currentTarget.style.transform = 'scale(1.05)'}
          onMouseLeave={(e) => e.currentTarget.style.transform = 'scale(1)'}
        >
          Wind down scene
        </Button>
        <Button
          variant="contained"
          style={{ 
            backgroundColor: '#64B5F6', 
            color: 'white', 
            fontSize: '18px', 
            letterSpacing: '0.75px', 
            fontWeight: 'bold',
            textTransform: 'none',
            borderRadius: '8px',
            boxShadow: '0px 4px 6px rgba(0, 0, 0, 0.1)',
            transition: 'transform 0.2s ease-in-out',
          }}
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
