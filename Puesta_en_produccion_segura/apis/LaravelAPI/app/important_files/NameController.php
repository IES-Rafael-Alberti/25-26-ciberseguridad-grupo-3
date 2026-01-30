<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class NameController extends Controller
{
    private $file = 'data.json';

    private function readData()
    {
        return json_decode(file_get_contents(base_path($this->file)), true);
    }

    private function writeData($data)
    {
        file_put_contents(base_path($this->file), json_encode($data, JSON_PRETTY_PRINT));
    }

    public function index()
    {
        return response()->json($this->readData());
    }

    public function saludo()
    {
        return response()->json(["message" => "Hola como estamos"]);
    }


    public function show($id)
    {
        $Names = $this->readData();
        $Name = collect($Names)->firstWhere('id', (int) $id);
        if (!$Name) return response()->json(['message' => 'Name not found'], 404);
        return response()->json($Name);
    }

    public function store(Request $request)
    {
        $Names = $this->readData();
        $Name = $request->all();
        $Name['id'] = count($Names) ? max(array_column($Names, 'id')) + 1 : 1;
        $Names[] = $Name;
        $this->writeData($Names);
        return response()->json($Name, 201);
    }

    public function update(Request $request, $id)
    {
        $Names = $this->readData();
        $index = collect($Names)->search(fn($i) => $i['id'] == (int)$id);
        if ($index === false) return response()->json(['message' => 'Name not found'], 404);
        $Names[$index] = array_merge($Names[$index], $request->all());
        $this->writeData($Names);
        return response()->json($Names[$index]);
    }

    public function destroy($id)
    {
        $Names = $this->readData();
        $index = collect($Names)->search(fn($i) => $i['id'] == (int)$id);
        if ($index === false) return response()->json(['message' => 'Name not found'], 404);
        array_splice($Names, $index, 1);
        $this->writeData($Names);
        return response()->json(null, 204);
    }
}
