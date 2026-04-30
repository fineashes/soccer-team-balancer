<?php
header('Content-Type: application/json');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: POST');
header('Access-Control-Allow-Headers: Content-Type');

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $input = file_get_contents('php://input');
    $player = json_decode($input, true);
    
    if ($player && isset($player['name']) && isset($player['position']) && isset($player['seed'])) {
        $csvFile = 'players.csv';
        $line = $player['name'] . ',' . $player['position'] . ',' . $player['seed'] . "\n";
        
        if (file_put_contents($csvFile, $line, FILE_APPEND | LOCK_EX)) {
            echo json_encode(['success' => true, 'message' => 'Player added successfully']);
        } else {
            http_response_code(500);
            echo json_encode(['success' => false, 'message' => 'Failed to write to CSV']);
        }
    } else {
        http_response_code(400);
        echo json_encode(['success' => false, 'message' => 'Invalid player data']);
    }
} else {
    http_response_code(405);
    echo json_encode(['success' => false, 'message' => 'Method not allowed']);
}
?>
