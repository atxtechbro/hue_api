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
            textTransform: 'none'
          }}
          onClick={() => triggerScene('/wind_down')}
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
            textTransform: 'none'
          }}
          onClick={() => triggerScene('/work_from_home')}
        >
          Work from home scene
        </Button>
      </Stack>
    </Box>
  );
}

export default Scenes;
